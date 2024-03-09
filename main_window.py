from PySide6.QtWidgets import *
import UI2Python.MainWindow_ui as mainUI
from manage_system import system_management as system
from utility.config_file_io import open_config_file, get_token
from utility.urls import Urls
import requests


class MainWindow(QMainWindow, mainUI.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.show()

        self.system_management_btn.enterEvent = self.show_account_describe
        self.neural_network_0_to_1_btn.enterEvent = self.show_nn_describe

        self.system_management_btn.clicked.connect(self.enter_system_management)

    def show_account_describe(self, event):
        self.md_textBrowser.setHtml(
            open_config_file(r'Template/EntryTemplate',r'Management.md', 'md')
        )

    def show_nn_describe(self, event):
        self.md_textBrowser.setHtml(
            open_config_file(r'Template/EntryTemplate', r'NeuralNetwork.md', 'md')
        )

    def enter_system_management(self):
        try:
            url = f'{Urls.LOGIN_API}'
            response = requests.get(
                url,
                headers={"Authorization": get_token(),"Content-Type": "application/json"}
            )
            if response.status_code == 200:
                self.close()
                self.system = system.SystemManagement()
                self.system.show()

            elif response.status_code == 401:
                QMessageBox.warning(self, "Warning", "沒有權限使用")

        except ConnectionError:
            QMessageBox.warning(self, "Warning", "連線失敗")
