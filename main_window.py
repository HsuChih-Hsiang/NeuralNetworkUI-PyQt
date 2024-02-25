import sys
from PySide6.QtWidgets import *
import UI2Python.MainWindow_ui as mainUI
from manage_system import login_system as login
from utility.ConfigFileIO import get_setting_path, open_md_file


class MainWindow(QMainWindow, mainUI.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.show()

        self.account_management_btn.enterEvent = self.show_account_describe
        self.neural_network_0_to_1.enterEvent = self.show_nn_describe

    def show_account_describe(self, event):
        self.md_textBrowser.setHtml(open_md_file(r'Template/EntryTemplate',r'Management.md'))

    def show_nn_describe(self, event):
        self.md_textBrowser.setHtml(open_md_file(r'Template/EntryTemplate',r'NeuralNetwork.md'))


if __name__ == '__main__':
    app = QApplication()
    login_ui = login.LoginDialog()
    login_ui.show()
    sys.exit(app.exec())
