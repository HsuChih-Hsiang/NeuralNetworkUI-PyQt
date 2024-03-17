from manage_system.label_dialog import AddLabelDialog
from manage_system.update_label_dialog import UpdateLabelDialog
import UI2Python.system_management_ui as system_management_ui
from utility.config_file_io import get_token
from utility.urls import Urls
import requests
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *


class SystemManagement(QWidget, system_management_ui.Ui_Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        # table widget setting
        self.setWindowTitle("system_management")
        self.header_text = [u"user_id", u"account", u"name", u"email", u"admin", u"read_only"]
        self.editable_header_text = [u"name", u"email", u"admin", u"read_only"]
        self.checkbox_header_text = [u"admin", u"read_only"]
        self.modify_row = set()

        self.initial_configuration()
        self.account_table.itemChanged.connect(self.catch_modify)
        self.edit_btn.clicked.connect(self.modify_account_info)

        # tabWidget setting
        self.tabWidget.currentChanged.connect(self.tab_change_init)

        # tree widget setting
        self.tree_header = ['name', 'layer', 'layer_id', 'is_description']
        self.get_data_header = ['layer', 'layer_id']

        self.treeWidget.setColumnCount(len(self.tree_header))
        self.treeWidget.setHeaderLabels(self.tree_header)
        self.treeWidget.itemExpanded.connect(self.get_node)

        # treeWidget menu
        self.treeWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.treeWidget.customContextMenuRequested.connect(self.side_menu)

        self.show()

    def tab_change_init(self):
        if self.tabWidget.currentIndex() == 0:
            self.initial_configuration()
        elif self.tabWidget.currentIndex() == 1:
            self.get_init_node()
        else:
            pass

    # 初始化設定
    def initial_setting(self):
        self.account_table.clear()
        # 防止因 inset row , row number 一直上升
        self.account_table.setRowCount(0)
        self.account_table.setColumnCount(len(self.header_text))
        self.account_table.setHorizontalHeaderLabels(self.header_text)

    def initial_configuration(self, response: requests = None):
        if response is None:
            url = f'{Urls.PERMISSION_API}'
            response = requests.get(url, headers={"Authorization": get_token(), "Content-Type": "application/json"})

        datas = response.json()
        account_data = datas.get('result', None)

        if response.status_code == 200:
            self.initial_setting()
            for row_cnt, row_data in enumerate(account_data):
                self.account_table.insertRow(row_cnt)
                for key, value in row_data.items():
                    col = self.header_text.index(key)
                    item = QTableWidgetItem(str(value))

                    if key not in self.editable_header_text:
                        # 設定為不可編輯
                        item.setFlags(Qt.ItemIsEditable)
                    if key in self.checkbox_header_text:
                        # 設定為 checkbox
                        if value:
                            item.setCheckState(Qt.Checked)
                        else:
                            item.setCheckState(Qt.Unchecked)
                        item.setText(str(value) if not isinstance(value, bool) else '')
                    self.account_table.setItem(row_cnt, col, item)
        else:
            QMessageBox.warning(self, "Warning", "權限不足或連線失敗")

    def closeEvent(self, event):
        from main_window import MainWindow
        self.main_window = MainWindow()
        self.main_window.show()

    def catch_modify(self):
        # 記住有改動的 row
        row_index = self.account_table.currentIndex()
        # TableWidget 將 item 轉為
        if row_index.row() >= 0:
            self.modify_row.add(row_index.row())

    def modify_account_info(self):
        try:
            modify_row = list(self.modify_row)
            data = list()
            for row in modify_row:
                row_data = list()
                for col in range(len(self.header_text)):
                    update_data = self.account_table.item(row, col)
                    if self.header_text[col] in self.checkbox_header_text:
                        state = update_data.checkState()
                        if state == Qt.Checked:
                            row_data.append(True)
                        else:
                            row_data.append(False)
                    elif self.header_text[col] == u'user_id':
                        row_data.append(int(update_data.text()))
                    else:
                        row_data.append(update_data.text())
                data.append(dict(zip(self.header_text, row_data)))
            # 清空修改過的 set
            self.modify_row = set()
            url = f'{Urls.PERMISSION_API}'
            response = requests.post(
                url,
                json={"permission_data": data},
                headers={"Authorization": get_token(), "Content-Type": "application/json"}
            )
            self.initial_configuration(response=response)

        except Exception as e:
            print(e)
            QMessageBox.warning(self, "Warning", text="未正確選取欄位")
            self.initial_configuration()

    def side_menu(self):
        self.menu = QMenu(self)
        self.menu.addAction("新增子節點", self.node_signal_1)
        self.menu.addAction("修改子節點", self.node_signal_2)
        self.menu.exec(QCursor.pos())

    def node_signal_1(self):
        self.label_dailog = AddLabelDialog()
        self.label_dailog.show()
        self.label_dailog.trans_label.connect(self.add_node)

    def node_signal_2(self):
        self.label_dailog = UpdateLabelDialog()
        self.label_dailog.show()
        self.label_dailog.trans_label.connect(self.update_node)

    def add_node(self, text):
        cur_item = self.treeWidget.currentItem()

        url = self.api_url_call(cur_item)

        if url:
            try:
                response = requests.post(
                    url,
                    json={"name": text},
                    headers={"Authorization": get_token(), "Content-Type": "application/json"}
                )

                if response.status_code == 200:
                    self.delete_old_node(cur_item)
                    node_list = response.json().get('result')
                    for node in node_list:
                        item = QTreeWidgetItem(cur_item)
                        self.node_display(item, node)

                elif response.status_code == 401:
                    QMessageBox.warning(self, "Warning", text="權限不足")

            except ConnectionError as e:
                print(e)
                QMessageBox.warning(self, "Warning", text="連線失敗")

    def update_node(self, text):
        cur_item = self.treeWidget.currentItem()

        url = self.api_url_call(cur_item)

        try:
            response = requests.put(
                url,
                json={},
                headers={"Authorization": get_token(), "Content-Type": "application/json"}
            )

            if response.status_code == 200:
                self.delete_old_node(cur_item)
                node_list = response.json().get('result')

                for node in node_list:
                    item = QTreeWidgetItem(cur_item)
                    self.node_display(item, node)

            elif response.status_code == 401:
                QMessageBox.warning(self, "Warning", text="權限不足")

        except ConnectionError as e:
            print(e)
            QMessageBox.warning(self, "Warning", text="連線失敗")

    def get_init_node(self):
        self.treeWidget.clear()
        try:
            url = f'{Urls.TOPIC_API}'
            response = requests.get(
                url,
                headers={"Authorization": get_token(), "Content-Type": "application/json"}
            )

            if response.status_code == 200:
                node_list = response.json().get('result')
                for node in node_list:
                    item = QTreeWidgetItem(self.treeWidget)
                    self.node_display(item, node)

            elif response.status_code == 401:
                QMessageBox.warning(self, "Warning", text="權限不足")

        except ConnectionError as e:
            print(e)
            QMessageBox.warning(self, "Warning", text="連線失敗")

    def get_node(self, expanded_item):
        self.delete_old_node(expanded_item)

        url = self.api_url_call(expanded_item)

        if url:
            try:
                response = requests.get(
                    url,
                    headers={"Authorization": get_token(), "Content-Type": "application/json"}
                )

                if response.status_code == 200:
                    node_list = response.json().get('result')
                    for node in node_list:
                        item = QTreeWidgetItem(expanded_item)
                        self.node_display(item, node)

                elif response.status_code == 401:
                    QMessageBox.warning(self, "Warning", text="權限不足")

            except ConnectionError as e:
                print(e)
                QMessageBox.warning(self, "Warning", text="連線失敗")

    # treeWidget sub function
    def api_url_call(self, item):
        url_data = dict()
        for data in self.get_data_header:
            index = self.tree_header.index(data)
            url_data.update(dict({data: item.text(index)}))

        layer = url_data.get('layer')
        layer_id = url_data.get('layer_id')

        if layer not in ['1', '2', '3']:
            return 0

        if layer == '1':
            url = f'{Urls.SUBTOPIC_API}/{layer_id}'
        elif layer == '2':
            url = f'{Urls.MODEL_CLASS_API}/{layer_id}'
        else:
            url = f'{Urls.MODEL_DETAIL_API}/{layer_id}'

        return url

    def node_display(self, cur_item, node):
        cur_item.setChildIndicatorPolicy(QTreeWidgetItem.ShowIndicator)
        for key, value in node.items():
            if key in self.tree_header:
                index = self.tree_header.index(key)
                if isinstance(value, bool):
                    if value:
                        cur_item.setCheckState(index, Qt.Checked)
                    else:
                        cur_item.setCheckState(index, Qt.Unchecked)
                else:
                    cur_item.setText(index, str(value))

    def delete_old_node(self, cur_item):
        for i in reversed(range(cur_item.childCount())):
            cur_item.takeChild(i)

