import UI2Python.update_label_dialog_ui as update_label_dialog_ui
from PySide6.QtWidgets import *
from PySide6.QtCore import *


class UpdateLabelDialog(QDialog, update_label_dialog_ui.Ui_Dialog):
    trans_label = Signal(str, bool, str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle('Label Dialog')
        self.buttonBox.accepted.connect(self.return_name)

        self.show()

    def return_name(self):
        label_name = self.label_name.text()
        self.trans_label.emit(label_name)
        self.accept()
