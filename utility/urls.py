from enum import Enum
from utility.config_file_io import open_config_file


class Urls(Enum):
    # Member
    LOGIN_API = 'member/login'
    REGISTER_API = 'member/register'
    PERMISSION_API = 'member/permission'

    # LayerLabel
    TOPIC_API = 'layer_label/topic'
    SUBTOPIC_API = 'layer_label/subtopic'
    MODEL_CLASS_API = 'layer_label/model_class'
    MODEL_DETAIL_API = 'layer_label/model_detail'

    def __format__(self, format_spec):
        env = open_config_file('setting', 'env.yaml', 'yaml')
        host = env.get('host')
        port = env.get('port')
        return f"{host}{f':{port}' if port else ''}/{self.value}"
