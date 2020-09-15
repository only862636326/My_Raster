# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_Frame_PlotCanvas.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Frame_PlotCanvas(object):
    def setupUi(self, Frame_PlotCanvas):
        Frame_PlotCanvas.setObjectName("Frame_PlotCanvas")
        Frame_PlotCanvas.resize(636, 494)
        self.gridLayout_2 = QtWidgets.QGridLayout(Frame_PlotCanvas)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Frame_PlotCanvas)
        QtCore.QMetaObject.connectSlotsByName(Frame_PlotCanvas)

    def retranslateUi(self, Frame_PlotCanvas):
        _translate = QtCore.QCoreApplication.translate
        Frame_PlotCanvas.setWindowTitle(_translate("Frame_PlotCanvas", "图象显示"))

