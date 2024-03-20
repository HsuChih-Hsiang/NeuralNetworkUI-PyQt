import UI2Python.label_url_dialog_ui as label_url_dialog_ui
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from utility.urls import ModeMapping


class LabelUrlDialog(QDialog, label_url_dialog_ui.Ui_Dialog):

    def __init__(self, layer, layer_id, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Mapping Label Url Dialog')

        self.check_box_data = list()
        self.layer = layer
        self.layer_id = layer_id

        self.enum_to_group_combobox()
        self.buttonBox.accepted.connect()

        self.show()

    def enum_to_group_combobox(self):
        model_mapping = ModeMapping.dict()

        for group_name, group_value in model_mapping.items():
            # add group box
            group_box = QGroupBox(group_name)
            self.verticalLayout.addWidget(group_box)

            # add layout in group box
            gridLayout = QGridLayout(group_box)
            verticalLayout = QVBoxLayout()
            gridLayout.addLayout(verticalLayout, 0, 0, 1, 1)
            for model_key, model_value in group_value.items():
                checkbox = QCheckBox(model_key)
                verticalLayout.addWidget(checkbox)
                checkbox.toggled.connect(lambda state: self.status_data(state, checkbox))

    def find_parent(self, widget):
        parent = widget.parentWidget()
        while parent:
            if isinstance(parent, QGroupBox):
                return parent.title()
            parent = widget.parentWidget()
        return None

    def status_data(self, status, checkbox):
        check = checkbox.text()
        group_box = self.find_parent(checkbox)

        if status:
            self.check_box_data.append((check, group_box))
        else:
            self.check_box_data.remove((check, group_box))

