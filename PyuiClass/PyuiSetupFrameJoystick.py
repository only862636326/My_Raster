# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Qtui/Qtui_frame_joystick.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FrameJoystick(object):
    def setupUi(self, FrameJoystick):
        FrameJoystick.setObjectName("FrameJoystick")
        FrameJoystick.resize(640, 441)
        font = QtGui.QFont()
        font.setPointSize(9)
        FrameJoystick.setFont(font)
        self.checkBox_L_up = QtWidgets.QCheckBox(FrameJoystick)
        self.checkBox_L_up.setGeometry(QtCore.QRect(240, 170, 71, 16))
        self.checkBox_L_up.setObjectName("checkBox_L_up")
        self.checkBox_L_down = QtWidgets.QCheckBox(FrameJoystick)
        self.checkBox_L_down.setGeometry(QtCore.QRect(210, 220, 71, 16))
        self.checkBox_L_down.setObjectName("checkBox_L_down")
        self.checkBox_R_down = QtWidgets.QCheckBox(FrameJoystick)
        self.checkBox_R_down.setGeometry(QtCore.QRect(370, 220, 71, 16))
        self.checkBox_R_down.setObjectName("checkBox_R_down")
        self.checkBox_R_up = QtWidgets.QCheckBox(FrameJoystick)
        self.checkBox_R_up.setGeometry(QtCore.QRect(340, 170, 71, 16))
        self.checkBox_R_up.setObjectName("checkBox_R_up")
        self.pushButton_W_L = QtWidgets.QPushButton(FrameJoystick)
        self.pushButton_W_L.setGeometry(QtCore.QRect(190, 130, 75, 23))
        self.pushButton_W_L.setObjectName("pushButton_W_L")
        self.pushButton_W_R = QtWidgets.QPushButton(FrameJoystick)
        self.pushButton_W_R.setGeometry(QtCore.QRect(360, 130, 75, 23))
        self.pushButton_W_R.setObjectName("pushButton_W_R")
        self.horizontalSlider_L_down = QtWidgets.QSlider(FrameJoystick)
        self.horizontalSlider_L_down.setGeometry(QtCore.QRect(140, 80, 160, 22))
        self.horizontalSlider_L_down.setMaximum(2048)
        self.horizontalSlider_L_down.setPageStep(1)
        self.horizontalSlider_L_down.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_L_down.setObjectName("horizontalSlider_L_down")
        self.horizontalSlider_R = QtWidgets.QSlider(FrameJoystick)
        self.horizontalSlider_R.setGeometry(QtCore.QRect(430, 30, 160, 22))
        self.horizontalSlider_R.setMaximum(2048)
        self.horizontalSlider_R.setPageStep(1)
        self.horizontalSlider_R.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_R.setObjectName("horizontalSlider_R")
        self.horizontalSlider_L_up = QtWidgets.QSlider(FrameJoystick)
        self.horizontalSlider_L_up.setGeometry(QtCore.QRect(140, 30, 160, 22))
        self.horizontalSlider_L_up.setMaximum(2048)
        self.horizontalSlider_L_up.setPageStep(1)
        self.horizontalSlider_L_up.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_L_up.setObjectName("horizontalSlider_L_up")
        self.label_P_L_up = QtWidgets.QLabel(FrameJoystick)
        self.label_P_L_up.setGeometry(QtCore.QRect(70, 30, 54, 12))
        self.label_P_L_up.setObjectName("label_P_L_up")
        self.label_P_L_down = QtWidgets.QLabel(FrameJoystick)
        self.label_P_L_down.setGeometry(QtCore.QRect(70, 80, 54, 12))
        self.label_P_L_down.setObjectName("label_P_L_down")
        self.label_P_R = QtWidgets.QLabel(FrameJoystick)
        self.label_P_R.setGeometry(QtCore.QRect(370, 30, 54, 12))
        self.label_P_R.setObjectName("label_P_R")
        self.pushButton_reset = QtWidgets.QPushButton(FrameJoystick)
        self.pushButton_reset.setGeometry(QtCore.QRect(460, 80, 75, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_reset.setFont(font)
        self.pushButton_reset.setStyleSheet("background-color: rgb(100, 255, 97);")
        self.pushButton_reset.setObjectName("pushButton_reset")
        self.label = QtWidgets.QLabel(FrameJoystick)
        self.label.setGeometry(QtCore.QRect(10, 160, 21, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(FrameJoystick)
        self.label_2.setGeometry(QtCore.QRect(430, 160, 21, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.layoutWidget = QtWidgets.QWidget(FrameJoystick)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 280, 239, 84))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_L_up = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_L_up.setObjectName("pushButton_L_up")
        self.gridLayout.addWidget(self.pushButton_L_up, 0, 1, 1, 1)
        self.pushButton_L_left = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_L_left.setObjectName("pushButton_L_left")
        self.gridLayout.addWidget(self.pushButton_L_left, 1, 0, 1, 1)
        self.pushButton_L_right = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_L_right.setObjectName("pushButton_L_right")
        self.gridLayout.addWidget(self.pushButton_L_right, 1, 2, 1, 1)
        self.pushButton_L_down = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_L_down.setObjectName("pushButton_L_down")
        self.gridLayout.addWidget(self.pushButton_L_down, 2, 1, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(FrameJoystick)
        self.layoutWidget1.setGeometry(QtCore.QRect(360, 280, 239, 83))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_R_up = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_R_up.setObjectName("pushButton_R_up")
        self.gridLayout_2.addWidget(self.pushButton_R_up, 0, 1, 1, 1)
        self.pushButton_R_left = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_R_left.setObjectName("pushButton_R_left")
        self.gridLayout_2.addWidget(self.pushButton_R_left, 1, 0, 1, 1)
        self.pushButton_R_right = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_R_right.setObjectName("pushButton_R_right")
        self.gridLayout_2.addWidget(self.pushButton_R_right, 1, 2, 1, 1)
        self.pushButton_R_down = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_R_down.setObjectName("pushButton_R_down")
        self.gridLayout_2.addWidget(self.pushButton_R_down, 2, 1, 1, 1)
        self.layoutWidget2 = QtWidgets.QWidget(FrameJoystick)
        self.layoutWidget2.setGeometry(QtCore.QRect(40, 150, 161, 88))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_Lx = QtWidgets.QLabel(self.layoutWidget2)
        self.label_Lx.setObjectName("label_Lx")
        self.verticalLayout.addWidget(self.label_Lx)
        self.horizontalSlider_Lx = QtWidgets.QSlider(self.layoutWidget2)
        self.horizontalSlider_Lx.setMinimum(-2048)
        self.horizontalSlider_Lx.setMaximum(2048)
        self.horizontalSlider_Lx.setPageStep(1)
        self.horizontalSlider_Lx.setSliderPosition(0)
        self.horizontalSlider_Lx.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_Lx.setObjectName("horizontalSlider_Lx")
        self.verticalLayout.addWidget(self.horizontalSlider_Lx)
        self.horizontalSlider_Ly = QtWidgets.QSlider(self.layoutWidget2)
        self.horizontalSlider_Ly.setMinimum(-2048)
        self.horizontalSlider_Ly.setMaximum(2048)
        self.horizontalSlider_Ly.setPageStep(1)
        self.horizontalSlider_Ly.setSliderPosition(0)
        self.horizontalSlider_Ly.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_Ly.setObjectName("horizontalSlider_Ly")
        self.verticalLayout.addWidget(self.horizontalSlider_Ly)
        self.label_Ly = QtWidgets.QLabel(self.layoutWidget2)
        self.label_Ly.setObjectName("label_Ly")
        self.verticalLayout.addWidget(self.label_Ly)
        self.layoutWidget3 = QtWidgets.QWidget(FrameJoystick)
        self.layoutWidget3.setGeometry(QtCore.QRect(460, 150, 161, 88))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_Rx = QtWidgets.QLabel(self.layoutWidget3)
        self.label_Rx.setObjectName("label_Rx")
        self.verticalLayout_2.addWidget(self.label_Rx)
        self.horizontalSlider_Rx = QtWidgets.QSlider(self.layoutWidget3)
        self.horizontalSlider_Rx.setMinimum(-2048)
        self.horizontalSlider_Rx.setMaximum(2048)
        self.horizontalSlider_Rx.setPageStep(1)
        self.horizontalSlider_Rx.setSliderPosition(0)
        self.horizontalSlider_Rx.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_Rx.setObjectName("horizontalSlider_Rx")
        self.verticalLayout_2.addWidget(self.horizontalSlider_Rx)
        self.horizontalSlider_Ry = QtWidgets.QSlider(self.layoutWidget3)
        self.horizontalSlider_Ry.setMinimum(-2048)
        self.horizontalSlider_Ry.setMaximum(2048)
        self.horizontalSlider_Ry.setPageStep(1)
        self.horizontalSlider_Ry.setSliderPosition(0)
        self.horizontalSlider_Ry.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_Ry.setObjectName("horizontalSlider_Ry")
        self.verticalLayout_2.addWidget(self.horizontalSlider_Ry)
        self.label_Ry = QtWidgets.QLabel(self.layoutWidget3)
        self.label_Ry.setObjectName("label_Ry")
        self.verticalLayout_2.addWidget(self.label_Ry)
        self.label_mode = QtWidgets.QLabel(FrameJoystick)
        self.label_mode.setGeometry(QtCore.QRect(290, 260, 75, 24))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_mode.setFont(font)
        self.label_mode.setText("")
        self.label_mode.setObjectName("label_mode")

        self.retranslateUi(FrameJoystick)
        QtCore.QMetaObject.connectSlotsByName(FrameJoystick)

    def retranslateUi(self, FrameJoystick):
        _translate = QtCore.QCoreApplication.translate
        FrameJoystick.setWindowTitle(_translate("FrameJoystick", "Frame"))
        self.checkBox_L_up.setText(_translate("FrameJoystick", "CheckBox"))
        self.checkBox_L_down.setText(_translate("FrameJoystick", "CheckBox"))
        self.checkBox_R_down.setText(_translate("FrameJoystick", "CheckBox"))
        self.checkBox_R_up.setText(_translate("FrameJoystick", "CheckBox"))
        self.pushButton_W_L.setText(_translate("FrameJoystick", "PushButton"))
        self.pushButton_W_R.setText(_translate("FrameJoystick", "PushButton"))
        self.label_P_L_up.setText(_translate("FrameJoystick", "0"))
        self.label_P_L_down.setText(_translate("FrameJoystick", "0"))
        self.label_P_R.setText(_translate("FrameJoystick", "0"))
        self.pushButton_reset.setText(_translate("FrameJoystick", "reset"))
        self.label.setText(_translate("FrameJoystick", "x\n"
"y"))
        self.label_2.setText(_translate("FrameJoystick", "x\n"
"y"))
        self.pushButton_L_up.setText(_translate("FrameJoystick", "PushButton"))
        self.pushButton_L_left.setText(_translate("FrameJoystick", "PushButton"))
        self.pushButton_L_right.setText(_translate("FrameJoystick", "PushButton"))
        self.pushButton_L_down.setText(_translate("FrameJoystick", "PushButton"))
        self.pushButton_R_up.setText(_translate("FrameJoystick", "PushButton"))
        self.pushButton_R_left.setText(_translate("FrameJoystick", "PushButton"))
        self.pushButton_R_right.setText(_translate("FrameJoystick", "PushButton"))
        self.pushButton_R_down.setText(_translate("FrameJoystick", "PushButton"))
        self.label_Lx.setText(_translate("FrameJoystick", "0"))
        self.label_Ly.setText(_translate("FrameJoystick", "0"))
        self.label_Rx.setText(_translate("FrameJoystick", "0"))
        self.label_Ry.setText(_translate("FrameJoystick", "0"))
