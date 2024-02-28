import UI2Python.system_management_ui as system_management
from utility.ConfigFileIO import get_token
import json
import sys
import requests
from PySide6.QtWidgets import *


class AccountManagementMainWindow(QWidget, system_management):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("system_management")
        # self.extra = extra

        self.initial_configuration()

        self.pushButton_refresh.clicked.connect(self.initial_configuration)
        self.pushButton_edit.clicked.connect(self.modify_account_info)
        self.pushButton_CreateAccount.clicked.connect(self.create_account)
        self.pushButton_AuthorityManagement.clicked.connect(self.authority_management)
        self.account_tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.account_tableWidget.customContextMenuRequested.connect(self.side_menu)

        self.show()

    # 初始化設定
    def initial_configuration(self):
        self.account_tableWidget.clearContents()
        url = "http://127.0.0.1/member/permission"
        response = requests.get(url, headers={"Authorization": get_token(), "Content-Type": "application/json"})
        db_json = response.json()
        arr = db_json["account_db"]

        # 根據現有 row 的數量決定要插入多少 row
        rows = self.account_tableWidget.rowCount()
        if rows < len(arr):
            for i in range(len(arr) - rows):
                # 讀取現在有幾個 row 後,再往後插入
                row_position = self.account_tableWidget.rowCount()
                self.account_tableWidget.insertRow(row_position)

        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if j <= 1:
                    item = QTableWidgetItem(str(arr[i][j]))
                    self.account_tableWidget.setItem(i, j, item)
                    if j == 0:
                        # 設定第一欄帳號無法被編輯
                        item.setFlags(Qt.ItemIsEditable)

                else:
                    item = QTableWidgetItem("")
                    # 根據原本的權限設定決定是否被 check
                    if arr[i][j]:
                        item.setCheckState(Qt.Checked)
                    else:
                        item.setCheckState(Qt.Unchecked)
                    self.account_tableWidget.setItem(i, j, item)

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
        cur_index = self.account_tableWidget.indexAt(pos)
        if cur_index.isValid():
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


if __name__ == "__main__":
    app = QApplication()
    account_management_window = AccountManagementMainWindow()
    sys.exit(app.exec())
