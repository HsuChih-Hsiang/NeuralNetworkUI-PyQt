import UI2Python.label_url_dialog_ui as label_url_dialog_ui
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from utility.urls import ModeMapping
import requests
from utility.config_file_io import get_token
from utility.urls import Urls


class LabelUrlDialog(QDialog, label_url_dialog_ui.Ui_Dialog):

    def __init__(self, layer, layer_id, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Mapping Label Url Dialog')

        self.check_box_data = list()
        self.layer = int(layer) + 1
        self.layer_id = int(layer_id)

        self.enum_to_group_combobox()

        self.show()

    def enum_to_group_combobox(self):
        model_mapping = ModeMapping.dict()
        data = None

        try:
            response = requests.get(
                f'{Urls.MODEL_MAPPING_API}',
                json={
                    'layer': self.layer,
                    'layer_id': self.layer_id
                },
                headers={"Authorization": get_token(), "Content-Type": "application/json"}
            )

            if response.status_code == 200:
                data = response.json().get('result')

            elif response.status_code == 400:
                QMessageBox.warning(self, "Warning", text="資料有誤")

            elif response.status_code == 401:
                QMessageBox.warning(self, "Warning", text="權限不足")

        except ConnectionError as e:
            print(e)
            QMessageBox.warning(self, "Warning", text="連線失敗")

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

                if data:
                    for layer_data in data:
                        api_name = layer_data.get('api_name')
                        if model_key == api_name:
                            checkbox.setCheckState(Qt.Checked)

                checkbox.toggled.connect(lambda status, text=checkbox.text(): self.status_data(text))
                verticalLayout.addWidget(checkbox)

    def status_data(self, checkbox):
        try:
            response = requests.put(
                f'{Urls.MODEL_MAPPING_API}',
                json={
                    'layer': self.layer,
                    'layer_id': self.layer_id,
                    'api_name': checkbox
                },
                headers={"Authorization": get_token(), "Content-Type": "application/json"}
            )

        except ConnectionError as e:
            print(e)

