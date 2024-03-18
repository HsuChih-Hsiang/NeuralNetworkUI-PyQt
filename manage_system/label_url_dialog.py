import UI2Python.label_url_dialog_ui as label_url_dialog_ui
from PySide6.QtWidgets import *
from PySide6.QtCore import *


class LabelUrlDialog(QDialog, label_url_dialog_ui.Ui_Dialog):

    def __init__(self, layer, layer_id, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Mapping Label Url Dialog')

        self.show()


