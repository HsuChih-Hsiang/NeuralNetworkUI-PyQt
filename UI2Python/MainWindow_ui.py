# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading main file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling main file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.neural_network_0_to_2 = QPushButton(self.centralwidget)
        self.neural_network_0_to_2.setObjectName(u"neural_network_0_to_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.neural_network_0_to_2.sizePolicy().hasHeightForWidth())
        self.neural_network_0_to_2.setSizePolicy(sizePolicy)
        self.neural_network_0_to_2.setMinimumSize(QSize(0, 40))
        self.neural_network_0_to_2.setSizeIncrement(QSize(0, 0))

        self.verticalLayout_2.addWidget(self.neural_network_0_to_2)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_5)

        self.account_management_btn_2 = QPushButton(self.centralwidget)
        self.account_management_btn_2.setObjectName(u"account_management_btn_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.account_management_btn_2.sizePolicy().hasHeightForWidth())
        self.account_management_btn_2.setSizePolicy(sizePolicy1)
        self.account_management_btn_2.setMinimumSize(QSize(0, 40))
        self.account_management_btn_2.setSizeIncrement(QSize(0, 0))
        self.account_management_btn_2.setBaseSize(QSize(0, 0))
        self.account_management_btn_2.setFocusPolicy(Qt.StrongFocus)
        self.account_management_btn_2.setContextMenuPolicy(Qt.NoContextMenu)
        self.account_management_btn_2.setInputMethodHints(Qt.ImhNone)
        self.account_management_btn_2.setAutoDefault(False)

        self.verticalLayout_2.addWidget(self.account_management_btn_2)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_6)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 4)

        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.neural_network_0_to_2.setText(QCoreApplication.translate("MainWindow", u"\u795e\u7d93\u7db2\u8def 0  to 1", None))
        self.account_management_btn_2.setText(QCoreApplication.translate("MainWindow", u"\u5e33\u865f\u6b0a\u9650\u7ba1\u7406", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

