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

    TOPIC_DETAIL_API = 'layer_label/topic/detail'
    SUBTOPIC_DETAIL_API = 'layer_label/subtopic/detail'
    MODEL_CLASS_DETAIL_API = 'layer_label/model_class/detail'
    MODEL_DETAIL_DESCRIPTION_API = 'layer_label/model_detail/detail'

    def __format__(self, format_spec):
        env = open_config_file('setting', 'env.yaml', 'yaml')
        host = env.get('host')
        port = env.get('port')
        return f"{host}{f':{port}' if port else ''}/{self.value}"


class BasicModelUrls(Enum):
    # Basic Model
    CNN_API = 'deep_learning/cnn'
    RNN_API = 'deep_learning/rnn'
    LSTM_API = 'deep_learning/lstm'

    @classmethod
    def dict(cls):
        env = open_config_file('setting', 'env.yaml', 'yaml')
        host = env.get('host')
        port = env.get('port')

        dictionary = {
            url.name: f"{host}{f':{port}' if port else ''}/{url.value}" for url in BasicModelUrls
        }

        return dictionary


class ModeMapping(Enum):
    # Basic Model
    Basic_Model_API = BasicModelUrls.dict()

    @classmethod
    def dict(cls):
        dictionary = {
            mapping.name: mapping.value for mapping in ModeMapping
        }
        return dictionary
