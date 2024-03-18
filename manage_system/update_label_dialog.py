import UI2Python.update_label_dialog_ui as update_label_dialog_ui
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from markdown import markdown


class UpdateLabelDialog(QDialog, update_label_dialog_ui.Ui_Dialog):
    # name, is_show. description
    trans_label = Signal(str, bool, str)

    def __init__(self, label_name, is_show, description, parent=None):
        super().__init__(parent,)
        self.setupUi(self)
        self.setWindowTitle('Update Label Dialog')
        self.buttonBox.accepted.connect(self.return_args)

        # params
        self.name = label_name
        self.is_show = is_show
        self.description = description

        # setting
        self.show_data()
        self.markdown_show()
        self.description_edit.textChanged.connect(self.markdown_show)

        self.show()

    def show_data(self):
        self.label_name.setText(self.name)
        self.is_show_checkBox.setChecked(self.is_show)
        self.description_edit.setPlainText(self.description)

    def markdown_show(self):
        description = self.description_edit.toPlainText()
        self.description_display.setHtml(markdown(description))

    def return_args(self):
        label_name = self.label_name.text()
        is_show = self.is_show_checkBox.isChecked()
        description = self.description_edit.toPlainText()
        self.trans_label.emit(label_name, is_show, description)
        self.accept()
