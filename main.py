import sys
from PySide6.QtWidgets import *
from manage_system import login_system as login


if __name__ == '__main__':
    app = QApplication()
    login_ui = login.LoginDialog()
    login_ui.show()
    sys.exit(app.exec())
