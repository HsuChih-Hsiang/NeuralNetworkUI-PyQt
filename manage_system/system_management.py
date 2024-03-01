import UI2Python.system_management_ui as system_management_ui
from utility.ConfigFileIO import get_token
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
        self.editable_header_text = [u"name", u"email",u"admin", u"read_only"]
        self.checkbox_header_text = [u"admin", u"read_only"]
        self.modify_row = set()

        self.initial_configuration()
        self.account_table.itemChanged.connect(self.catch_modify)
        self.edit_btn.clicked.connect(self.modify_account_info)

        # tree widget setting
        self.account_table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.account_table.customContextMenuRequested.connect(self.side_menu)

        self.show()

    # 初始化設定
    def initial_setting(self):
        self.account_table.clear()
        # 防止因 inset row , row number 一直上升
        self.account_table.setRowCount(0)
        self.account_table.setColumnCount(len(self.header_text))
        self.account_table.setHorizontalHeaderLabels(self.header_text)

    def initial_configuration(self, response:requests = None):
        if response is None:
            url = "http://127.0.0.1:8000/member/permission"
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
        self.mainwindow = MainWindow()
        self.mainwindow.show()

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
            url = "http://127.0.0.1:8000/member/permission"
            response = requests.post(
                url,
                json={"permission_data": data},
                headers={"Authorization": get_token(), "Content-Type": "application/json"}
            )
            self.initial_configuration(response=response)

        except Exception as e:
            QMessageBox.warning(self, "Warning", "未正確選取欄位")
            self.initial_configuration()

    def side_menu(self):
        menu = QMenu()
        action_1 = QAction("修改密碼")
        menu.addAction(action_1)
        action_2 = QAction("不修改密碼")
        menu.addAction(action_2)
        action_1.triggered.connect(self.change_password_dialog)
        menu.exec(QCursor.pos())

    def change_password_dialog(self):
        # 取得目前所要更改密碼的帳號及使用者
        row_index = self.account_tableWidget.currentIndex()
        self.account = self.account_tableWidget.item(row_index.row(), 0).text()
        self.user = self.account_tableWidget.item(row_index.row(), 1).text()
        self.cpm = ChangePasswordMainWindow(account=self.account, user=self.user)
