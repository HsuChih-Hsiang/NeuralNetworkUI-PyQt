import sys
from PySide6.QtWidgets import *
import requests
import UI2Python.create_account_ui as register_ui


class RegisterDialog(QDialog, register_ui.Ui_Dialog):
    def __init__(self):
        super(RegisterDialog, self).__init__()
        self.setupUi(self)

        self.setWindowTitle('Register')
