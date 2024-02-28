# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTextBrowser, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(780, 570)
        MainWindow.setMinimumSize(QSize(780, 570))
        MainWindow.setMaximumSize(QSize(780, 570))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.system_management_btn = QPushButton(self.centralwidget)
        self.system_management_btn.setObjectName(u"system_management_btn")
        self.system_management_btn.setGeometry(QRect(0, 90, 211, 91))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.system_management_btn.sizePolicy().hasHeightForWidth())
        self.system_management_btn.setSizePolicy(sizePolicy)
        self.system_management_btn.setMinimumSize(QSize(0, 40))
        self.system_management_btn.setSizeIncrement(QSize(0, 0))
        self.system_management_btn.setBaseSize(QSize(0, 0))
        self.system_management_btn.setFocusPolicy(Qt.StrongFocus)
        self.system_management_btn.setContextMenuPolicy(Qt.NoContextMenu)
        self.system_management_btn.setInputMethodHints(Qt.ImhNone)
        self.system_management_btn.setAutoDefault(False)
        self.neural_network_0_to_1_btn = QPushButton(self.centralwidget)
        self.neural_network_0_to_1_btn.setObjectName(u"neural_network_0_to_1_btn")
        self.neural_network_0_to_1_btn.setGeometry(QRect(0, 0, 211, 91))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.neural_network_0_to_1_btn.sizePolicy().hasHeightForWidth())
        self.neural_network_0_to_1_btn.setSizePolicy(sizePolicy1)
        self.neural_network_0_to_1_btn.setMinimumSize(QSize(0, 40))
        self.neural_network_0_to_1_btn.setSizeIncrement(QSize(0, 0))
        self.md_textBrowser = QTextBrowser(self.centralwidget)
        self.md_textBrowser.setObjectName(u"md_textBrowser")
        self.md_textBrowser.setGeometry(QRect(220, 0, 551, 521))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 780, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.system_management_btn.setText(QCoreApplication.translate("MainWindow", u"\u61c9\u7528\u7a0b\u5f0f\u7ba1\u7406", None))
        self.neural_network_0_to_1_btn.setText(QCoreApplication.translate("MainWindow", u"\u795e\u7d93\u7db2\u8def 0  to 1", None))
    # retranslateUi

