import sys
from PySide6.QtWidgets import *
import requests
import UI2Python.login_ui as login_ui


class LoginDialog(QDialog, login_ui.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle('Login')
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
            info = QMessageBox.information(self,"Info","登入成功")

            if info == self.accept():
                pass

        else:
            QMessageBox.warning(self,"Warning", "登入失敗")


if __name__ == '__main__':
    app = QApplication()
    login_ui = LoginDialog()
    login_ui.show()
    sys.exit(app.exec())
