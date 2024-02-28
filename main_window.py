from PySide6.QtWidgets import *
import UI2Python.MainWindow_ui as mainUI
from manage_system import system_management as system
from utility.ConfigFileIO import open_md_file


class MainWindow(QMainWindow, mainUI.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.show()

        self.system_management_btn.enterEvent = self.show_account_describe
        self.neural_network_0_to_1_btn.enterEvent = self.show_nn_describe

        self.system_management_btn.clicked.connect(self.enter_system_management)

    def show_account_describe(self, event):
        self.md_textBrowser.setHtml(open_md_file(r'Template/EntryTemplate',r'Management.md'))

    def show_nn_describe(self, event):
        self.md_textBrowser.setHtml(open_md_file(r'Template/EntryTemplate',r'NeuralNetwork.md'))

    def enter_system_management(self):
        self.close()
        self.system = system.SystemManagement()
        self.system.show()
