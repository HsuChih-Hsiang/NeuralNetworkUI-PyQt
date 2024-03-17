import UI2Python.update_label_dialog_ui as update_label_dialog_ui
from PySide6.QtWidgets import *
from PySide6.QtCore import *


class UpdateLabelDialog(QDialog, update_label_dialog_ui.Ui_Dialog):
    # name, is_show. description
    trans_label = Signal(str, bool, str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle('Update Label Dialog')
        self.buttonBox.accepted.connect(self.return_args)

        self.show()

    def return_args(self):
        label_name = self.label_name.text()
        is_show = self.is_show_checkBox.isChecked()
        description = self.description_edit.toPlainText()
        self.trans_label.emit(label_name, is_show, description)
        self.accept()
