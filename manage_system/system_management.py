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
        self.setWindowTitle("system_management")
        self.header_text = [u"user_id", u"account", u"name", u"admin", u"read_only"]
        self.editable_header_text = [u"name", u"admin", u"read_only"]
        self.checkbox_header_text = [u"admin", u"read_only"]

        self.initial_configuration()
        # self.pushButton_edit.clicked.connect(self.modify_account_info)
        # self.pushButton_CreateAccount.clicked.connect(self.create_account)
        # self.pushButton_AuthorityManagement.clicked.connect(self.authority_management)
        # self.account_tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        # self.account_tableWidget.customContextMenuRequested.connect(self.side_menu)

        self.show()

    # 初始化設定
    def initial_configuration(self):
        self.account_table.clear()
        self.account_table.setColumnCount(len(self.header_text))
        self.account_table.setHorizontalHeaderLabels(self.header_text)
        url = "http://127.0.0.1:8000/member/permission"
        response = requests.get(url, headers={"Authorization": get_token(), "Content-Type": "application/json"})
        datas = response.json()
        account_data = datas.get('result', None)

        if response.status_code == 200:
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
                        value = bool(value)
                        if value:
                            value = ''
                            item.setCheckState(Qt.Checked)
                        else:
                            value = ''
                            item.setCheckState(Qt.Unchecked)
                    item.setText(str(value))
                    self.account_table.setItem(row_cnt, col, item)
        else:
            QMessageBox.warning(self, "Warning", "權限不足或連線失敗")

    def register_window(self):
        from main_window import MainWindow
        self.close()
        self.mainwindow = MainWindow()
        self.mainwindow.show()

    def modify_account_info(self):
        url2 = f"http://{host}/permission_setting"
        columns = self.account_tableWidget.columnCount()
        rows = self.account_tableWidget.rowCount()
        data_temp = []
        for row in range(rows):
            temp = []
            for column in range(columns):
                if column <= 1:
                    temp.append(self.account_tableWidget.item(row, column).text())
                else:
                    is_checked = (
                            self.account_tableWidget.item(row, column).checkState()
                            == Qt.Checked
                    )
                    temp.append(is_checked)
                    if column == columns - 1:
                        data_temp.append(temp)

        payloads = {"account_data": data_temp}

        mes = requests.request("POST", url2, json=payloads, headers={})

        if mes.text == "OK":
            QMessageBox.question(self, "提示", "帳號修改成功")
        else:
            QMessageBox.question(self, "提示", "帳號未修改成功")

    def manage_account_settings(self):
        index = self.account_tableWidget.currentIndex()
        if (
                index.column() == 6
                and self.account_tableWidget.item(index.row(), index.column()).checkState()
                == Qt.Checked
        ):
            for i in range(4, 6):
                item = QTableWidgetItem("")
                item.setCheckState(Qt.Checked)
                self.account_tableWidget.setItem(index.row(), i, item)

    def side_menu(self, pos):
        menu = QMenu()
        action_1 = QAction("修改密碼")
        menu.addAction(action_1)
        action_1.triggered.connect(self.change_password_dialog)
        menu.exec(QCursor.pos())

    def change_password_dialog(self):
        # 取得目前所要更改密碼的帳號及使用者
        row_index = self.account_tableWidget.currentIndex()
        self.account = self.account_tableWidget.item(row_index.row(), 0).text()
        self.user = self.account_tableWidget.item(row_index.row(), 1).text()
        self.cpm = ChangePasswordMainWindow(account=self.account, user=self.user)
