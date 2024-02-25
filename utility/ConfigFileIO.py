import yaml
from markdown import markdown
import os


def get_setting_path(file_dir: str = 'setting', file_name: str = 'config.yaml') -> str:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent = os.path.join(current_dir, os.pardir)
    settings_dir = os.path.join(parent, file_dir)
    filename = file_name
    settings_path = os.path.join(settings_dir, filename)
    return settings_path


def save_token(token: dict):
    try:
        with open(get_setting_path(), mode='w+') as old_setting:
            data = yaml.load(old_setting, Loader=yaml.FullLoader)
            data = data.update(token) if data is not None else token
            yaml.dump(data, old_setting, default_flow_style=False, allow_unicode=True)
            old_setting.close()
        return True
    except IOError as e:
        return False


def get_token():
    try:
        with open(get_setting_path()) as token:
            data = yaml.load(token, Loader=yaml.FullLoader)
        return data.get('token', None)

    except IOError as e:
        return None


def open_md_file(file_dir: str, file_name: str):
    try:
        with open(get_setting_path(file_dir, file_name), 'r', encoding="utf-8") as file:
            data = markdown(file.read())

        return data

    except IOError as e:
        return False
