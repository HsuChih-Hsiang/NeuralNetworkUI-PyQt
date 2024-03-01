import UI2Python.create_account_ui as register_ui
from PySide6.QtWidgets import *
import requests
import UI2Python.login_ui as login_ui
from main_window import MainWindow
from utility.ConfigFileIO import save_token


class LoginDialog(QDialog, login_ui.Ui_Dialog):
    def __init__(self):
        super(LoginDialog, self).__init__()
        self.setupUi(self)

        self.setWindowTitle('Login')
        self.login_btn.clicked.connect(self.login_fuc)
        self.regist_btn.clicked.connect(self.register_window)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

    def login_fuc(self):
        url = "http://127.0.0.1:8000/member/login"
        account = self.account_input.text()
        password = self.password_input.text()

        payloads = {"account": account, "password": password}
        response = requests.post(
            url,
            json=payloads,
            headers={"Content-Type": "application/json"}
        )

        if response.status_code == 200:
            QMessageBox.information(self, "Info", "登入成功")
            self.accept()

            result = save_token(response.json().get('result'))
            if result:
                # 利用 self 將其 instance, 否則依執行就會被回收
                # 寫在 __init__ 會在執行時直接出現畫面
                self.main_win = MainWindow()
                self.main_win.show()
            else:
                QMessageBox.warning(self, "Warning", "config 檔缺失或所毀,請檢查檔案正確性")

        else:
            QMessageBox.warning(self, "Warning", "登入失敗")

    def register_window(self):
        self.close()
        self.register_ui = RegisterDialog()
        self.register_ui.show()


class RegisterDialog(QDialog, register_ui.Ui_Dialog):
    def __init__(self):
        super(RegisterDialog, self).__init__()
        self.setupUi(self)

        self.setWindowTitle('Register')
        self.password_lineEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.compassword_lineEdit.setEchoMode(QLineEdit.EchoMode.Password)

        self.confirm_btn.clicked.connect(self.register_func)

    def closeEvent(self, event):
        self.login_ui = LoginDialog()
        self.login_ui.show()

    def register_func(self):
        url = "http://127.0.0.1:8000/member/register"
        account = self.account_lineEdit.text()
        password = self.password_lineEdit.text()
        confirm_password = self.compassword_lineEdit.text()
        name = self.name_lineEdit.text()
        email = self.email_lineEdit.text()

        if password != confirm_password:
            QMessageBox.warning(self, "Warning", "密碼不一致")

        else:
            payloads = {"account": account, "password": password, "name": name}

            if email:
                payloads.update({'email': email})

            response = requests.post(
                url,
                json=payloads,
                headers={"content-type": "application/json"}
            )

            if response.status_code == 200:
                QMessageBox.information(self, "Info", "註冊成功")
                self.accept()
                result = save_token(response.json().get('result'))

                if result:
                    # 利用 self 將其 instance, 否則依執行就會被回收
                    # 寫在 __init__ 會在執行時直接出現畫面
                    self.main_win = MainWindow()
                    self.main_win.show()
                else:
                    QMessageBox.warning(self, "Warning", "config 檔缺失或所毀,請檢查檔案正確性")

            elif response.status_code == 400:
                QMessageBox.warning(self, "Warning", "註冊失敗")
