# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UiDialogYesNo.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogYesNo(object):
    def setupUi(self, DialogYesNo):
        DialogYesNo.setObjectName("DialogYesNo")
        DialogYesNo.resize(391, 144)
        DialogYesNo.setWindowFilePath("")
        self.buttonBox = QtWidgets.QDialogButtonBox(DialogYesNo)
        self.buttonBox.setGeometry(QtCore.QRect(20, 90, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_msg = QtWidgets.QLabel(DialogYesNo)
        self.label_msg.setGeometry(QtCore.QRect(50, 20, 291, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_msg.setFont(font)
        self.label_msg.setStyleSheet("")
        self.label_msg.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_msg.setAlignment(QtCore.Qt.AlignCenter)
        self.label_msg.setObjectName("label_msg")

        self.retranslateUi(DialogYesNo)
        self.buttonBox.accepted.connect(DialogYesNo.accept)
        self.buttonBox.rejected.connect(DialogYesNo.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogYesNo)

    def retranslateUi(self, DialogYesNo):
        _translate = QtCore.QCoreApplication.translate
        DialogYesNo.setWindowTitle(_translate("DialogYesNo", "DialogYesNo"))
        self.label_msg.setText(_translate("DialogYesNo", "数据错误"))
