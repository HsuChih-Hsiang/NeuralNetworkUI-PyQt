# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'system_management.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QHeaderView,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QTableWidget, QTableWidgetItem, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(820, 328)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.account_table = QTableWidget(self.tab)
        if (self.account_table.columnCount() < 5):
            self.account_table.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.account_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.account_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.account_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.account_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.account_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.account_table.setObjectName(u"account_table")

        self.gridLayout_2.addWidget(self.account_table, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.edit_btn = QPushButton(self.tab)
        self.edit_btn.setObjectName(u"edit_btn")

        self.verticalLayout.addWidget(self.edit_btn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_4 = QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.edit_description_btn = QPushButton(self.tab_2)
        self.edit_description_btn.setObjectName(u"edit_description_btn")

        self.gridLayout_4.addWidget(self.edit_description_btn, 2, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(583, 21, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.delete_btn = QPushButton(self.tab_2)
        self.delete_btn.setObjectName(u"delete_btn")

        self.gridLayout_4.addWidget(self.delete_btn, 2, 1, 1, 1)

        self.treeWidget = QTreeWidget(self.tab_2)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.treeWidget.setProperty("showDropIndicator", True)

        self.gridLayout_4.addWidget(self.treeWidget, 1, 0, 1, 3)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        ___qtablewidgetitem = self.account_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"id", None));
        ___qtablewidgetitem1 = self.account_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"account", None));
        ___qtablewidgetitem2 = self.account_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"name", None));
        ___qtablewidgetitem3 = self.account_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"admin", None));
        ___qtablewidgetitem4 = self.account_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"read_only", None));
        self.edit_btn.setText(QCoreApplication.translate("Form", u"\u9001\u51fa\u4fee\u6539", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"\u5e33\u865f\u7ba1\u7406", None))
        self.edit_description_btn.setText(QCoreApplication.translate("Form", u"\u4fee\u6539\u5167\u5bb9\u63cf\u8ff0", None))
        self.delete_btn.setText(QCoreApplication.translate("Form", u"\u522a\u9664\u52fe\u9078\u9805\u76ee", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("Form", u"have_description", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("Form", u"layer_id", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Form", u"label", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"\u6df1\u5ea6\u5b78\u7fd2\u5167\u5bb9\u7ba1\u7406", None))
    # retranslateUi

