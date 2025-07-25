# Form implementation generated from reading ui file '.\ui\main_screen.ui'
#
# Created by: PyQt6 UI code generator 6.9.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1164, 869)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_nav_wid = QtWidgets.QWidget(parent=self.centralwidget)
        self.top_nav_wid.setObjectName("top_nav_wid")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.top_nav_wid)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, 80, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mm_lbl = QtWidgets.QLabel(parent=self.top_nav_wid)
        self.mm_lbl.setObjectName("mm_lbl")
        self.horizontalLayout.addWidget(self.mm_lbl)
        self.horizontalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.sys_icon = QtWidgets.QLabel(parent=self.top_nav_wid)
        self.sys_icon.setMinimumSize(QtCore.QSize(20, 20))
        self.sys_icon.setMaximumSize(QtCore.QSize(20, 20))
        self.sys_icon.setText("")
        self.sys_icon.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.sys_icon.setPixmap(QtGui.QPixmap(":/newPrefix/images/sys_icon.png"))
        self.sys_icon.setScaledContents(True)
        self.sys_icon.setWordWrap(True)
        self.sys_icon.setObjectName("sys_icon")
        self.horizontalLayout_2.addWidget(self.sys_icon)
        self.sys_lbl = QtWidgets.QLabel(parent=self.top_nav_wid)
        self.sys_lbl.setObjectName("sys_lbl")
        self.horizontalLayout_2.addWidget(self.sys_lbl)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.func_icon = QtWidgets.QLabel(parent=self.top_nav_wid)
        self.func_icon.setMinimumSize(QtCore.QSize(20, 20))
        self.func_icon.setMaximumSize(QtCore.QSize(20, 20))
        self.func_icon.setText("")
        self.func_icon.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.func_icon.setPixmap(QtGui.QPixmap(":/newPrefix/images/func_icon.png"))
        self.func_icon.setScaledContents(True)
        self.func_icon.setWordWrap(True)
        self.func_icon.setObjectName("func_icon")
        self.horizontalLayout_3.addWidget(self.func_icon)
        self.func_lbl = QtWidgets.QLabel(parent=self.top_nav_wid)
        self.func_lbl.setObjectName("func_lbl")
        self.horizontalLayout_3.addWidget(self.func_lbl)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.data_icon = QtWidgets.QLabel(parent=self.top_nav_wid)
        self.data_icon.setMinimumSize(QtCore.QSize(20, 20))
        self.data_icon.setMaximumSize(QtCore.QSize(20, 20))
        self.data_icon.setText("")
        self.data_icon.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.data_icon.setPixmap(QtGui.QPixmap(":/newPrefix/images/data_icon.png"))
        self.data_icon.setScaledContents(True)
        self.data_icon.setWordWrap(True)
        self.data_icon.setObjectName("data_icon")
        self.horizontalLayout_4.addWidget(self.data_icon)
        self.data_lbl = QtWidgets.QLabel(parent=self.top_nav_wid)
        self.data_lbl.setObjectName("data_lbl")
        self.horizontalLayout_4.addWidget(self.data_lbl)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.top_nav_wid)
        self.main_wid = QtWidgets.QWidget(parent=self.centralwidget)
        self.main_wid.setObjectName("main_wid")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.main_wid)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout.addWidget(self.main_wid)
        self.ctrl_wid = QtWidgets.QWidget(parent=self.centralwidget)
        self.ctrl_wid.setObjectName("ctrl_wid")
        self.ctrl_layout = QtWidgets.QHBoxLayout(self.ctrl_wid)
        self.ctrl_layout.setContentsMargins(0, 0, 0, 0)
        self.ctrl_layout.setObjectName("ctrl_layout")
        self.verticalLayout.addWidget(self.ctrl_wid)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 20)
        self.verticalLayout.setStretch(2, 15)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.mm_lbl.setText(_translate("MainWindow", "MM treadmill system"))
        self.sys_lbl.setText(_translate("MainWindow", "System"))
        self.func_lbl.setText(_translate("MainWindow", "Function"))
        self.data_lbl.setText(_translate("MainWindow", "Data"))
