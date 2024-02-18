import sys
from PySide6.QtWidgets import *
import requests
import UI2Python.login_ui as login_ui


class LoginDialog(QDialog, login_ui.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle('登入')
        self.login_btn.clicked.connect(self.login_fuc)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

    def login_fuc(self):
        url = "http://127.0.0.1:8000/member/login"
        account = self.account_input.text()
        password = self.password_input.text()

        payloads = {"account": account, "password": password}
        response = requests.post(
            url,
            json=payloads,
            headers={"content-type": "application/json"}
        )

        if response.status_code == 200:
            QMessageBox.information(self, "登入", "登入成功")
            return self.accept()
        else:
            QMessageBox.warning(self, "登入", "登入失敗")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_ui = LoginDialog()
    login_ui.show()
    sys.exit(app.exec())
