# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_account.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(260, 184)
        Dialog.setMinimumSize(QSize(260, 184))
        Dialog.setMaximumSize(QSize(260, 184))
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(50, 0))
        self.label_4.setMaximumSize(QSize(16777215, 16777215))
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.name_lineEdit = QLineEdit(Dialog)
        self.name_lineEdit.setObjectName(u"name_lineEdit")
        self.name_lineEdit.setMaxLength(50)

        self.horizontalLayout_4.addWidget(self.name_lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_1 = QLabel(Dialog)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setMinimumSize(QSize(50, 0))
        self.label_1.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setWeight(QFont.Medium)
        self.label_1.setFont(font)
        self.label_1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_1)

        self.account_lineEdit = QLineEdit(Dialog)
        self.account_lineEdit.setObjectName(u"account_lineEdit")
        self.account_lineEdit.setMaximumSize(QSize(16777215, 16777215))
        self.account_lineEdit.setMaxLength(20)

        self.horizontalLayout.addWidget(self.account_lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(50, 0))
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_5)

        self.email_lineEdit = QLineEdit(Dialog)
        self.email_lineEdit.setObjectName(u"email_lineEdit")
        self.email_lineEdit.setMaxLength(20)

        self.horizontalLayout_5.addWidget(self.email_lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(50, 0))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.password_lineEdit = QLineEdit(Dialog)
        self.password_lineEdit.setObjectName(u"password_lineEdit")
        self.password_lineEdit.setMaxLength(20)

        self.horizontalLayout_3.addWidget(self.password_lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(50, 0))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.compassword_lineEdit = QLineEdit(Dialog)
        self.compassword_lineEdit.setObjectName(u"compassword_lineEdit")
        self.compassword_lineEdit.setMaxLength(20)

        self.horizontalLayout_2.addWidget(self.compassword_lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.confirm_btn = QPushButton(Dialog)
        self.confirm_btn.setObjectName(u"confirm_btn")

        self.gridLayout.addWidget(self.confirm_btn, 1, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u59d3\u540d", None))
        self.label_1.setText(QCoreApplication.translate("Dialog", u"\u5e33\u865f", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u96fb\u5b50\u4fe1\u7bb1", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u5bc6\u78bc", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u78ba\u8a8d\u5bc6\u78bc", None))
        self.confirm_btn.setText(QCoreApplication.translate("Dialog", u"\u78ba\u8a8d", None))
    # retranslateUi

