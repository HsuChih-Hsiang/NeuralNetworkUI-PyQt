import sys
from PySide6.QtWidgets import *
import requests
import UI2Python.MainWindow_ui as mainUI
import LoginSystem.login as login

# import register


class MainWindow(QMainWindow, mainUI.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.show()


if __name__ == '__main__':
    app = QApplication()
    login_ui = login.LoginDialog()
    login_ui.show()
    sys.exit(app.exec())
