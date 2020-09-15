# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UiDialogMsg.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogMsg(object):
    def setupUi(self, DialogMsg):
        DialogMsg.setObjectName("DialogMsg")
        DialogMsg.resize(369, 116)
        self.label_msg = QtWidgets.QLabel(DialogMsg)
        self.label_msg.setGeometry(QtCore.QRect(30, 10, 311, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_msg.setFont(font)
        self.label_msg.setStyleSheet("")
        self.label_msg.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_msg.setAlignment(QtCore.Qt.AlignCenter)
        self.label_msg.setObjectName("label_msg")

        self.retranslateUi(DialogMsg)
        QtCore.QMetaObject.connectSlotsByName(DialogMsg)

    def retranslateUi(self, DialogMsg):
        _translate = QtCore.QCoreApplication.translate
        DialogMsg.setWindowTitle(_translate("DialogMsg", "DialogMsg"))
        self.label_msg.setText(_translate("DialogMsg", "数据错误"))
