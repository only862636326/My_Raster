# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Qtui/Qtui_frame_ser_control.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FrameSerControl(object):
    def setupUi(self, FrameSerControl):
        FrameSerControl.setObjectName("FrameSerControl")
        FrameSerControl.resize(197, 68)
        font = QtGui.QFont()
        font.setPointSize(12)
        FrameSerControl.setFont(font)
        FrameSerControl.setStyleSheet("background-color: rgb(196, 196, 255);")
        self.comboBox_com_choose = QtWidgets.QComboBox(FrameSerControl)
        self.comboBox_com_choose.setGeometry(QtCore.QRect(60, 10, 81, 25))
        self.comboBox_com_choose.setMaximumSize(QtCore.QSize(100, 16777215))
        self.comboBox_com_choose.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox_com_choose.setFont(font)
        self.comboBox_com_choose.setObjectName("comboBox_com_choose")
        self.comboBox_com_choose.addItem("")
        self.pushButton_open = QtWidgets.QPushButton(FrameSerControl)
        self.pushButton_open.setGeometry(QtCore.QRect(140, 10, 51, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_open.setFont(font)
        self.pushButton_open.setStyleSheet("background-color: rgb(69, 255, 97);")
        self.pushButton_open.setObjectName("pushButton_open")
        self.pushButton_close = QtWidgets.QPushButton(FrameSerControl)
        self.pushButton_close.setGeometry(QtCore.QRect(160, 10, 41, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_close.setFont(font)
        self.pushButton_close.setStyleSheet("background-color: rgb(255, 7, 11);")
        self.pushButton_close.setObjectName("pushButton_close")
        self.label_ser_info = QtWidgets.QLabel(FrameSerControl)
        self.label_ser_info.setGeometry(QtCore.QRect(60, 40, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_ser_info.setFont(font)
        self.label_ser_info.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_ser_info.setStyleSheet("background-color: rgb(167, 255, 153);")
        self.label_ser_info.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ser_info.setObjectName("label_ser_info")
        self.label_2 = QtWidgets.QLabel(FrameSerControl)
        self.label_2.setGeometry(QtCore.QRect(0, 30, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setStyleSheet("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(FrameSerControl)
        self.label.setGeometry(QtCore.QRect(10, 10, 48, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(FrameSerControl)
        QtCore.QMetaObject.connectSlotsByName(FrameSerControl)

    def retranslateUi(self, FrameSerControl):
        _translate = QtCore.QCoreApplication.translate
        FrameSerControl.setWindowTitle(_translate("FrameSerControl", "Frame"))
        self.comboBox_com_choose.setItemText(0, _translate("FrameSerControl", "COM18"))
        self.pushButton_open.setText(_translate("FrameSerControl", "打开"))
        self.pushButton_close.setText(_translate("FrameSerControl", "关闭"))
        self.label_ser_info.setText(_translate("FrameSerControl", "当前信息"))
        self.label_2.setText(_translate("FrameSerControl", "仅当串口\n"
"不在使用时\n"
"可自动检测"))
        self.label.setText(_translate("FrameSerControl", "串口选择"))
