# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QFrame
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer, Qt

from MyClass import MyClassSerial, MyClassPack, MyClassQtTreadReadBit, MyClassQtTreadReadPack, MyClassQtTreadReadLine
from PyuiClass.PyuiSetupFrameJoystick import Ui_FrameJoystick

from PyuiClass.PyuiClassFrameSerControlkFile import PyuiClassFrameSerControl

import matplotlib.pyplot as plt
# import numpy as np

class PyuiClassFrameJoystick(QFrame,Ui_FrameJoystick):

    def __init__(self, ser:'MyClassSerial' = None, show = False):
        super(PyuiClassFrameJoystick, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowMinimizeButtonHint|Qt.WindowCloseButtonHint)
        self.setFixedSize(self.width(), self.height())
        self.dead_band = 300
        self.joystick = [0,0,0,0, 0,0,0, 0,0]
        pack = MyClassPack(r'=hhhhhhhBB', b'\xAA', b'\x55', b'\x55', b'\xAA')

        if isinstance(ser, MyClassSerial):
            self.ser = ser
            self.ser.change_pack(pack)
        else:
            self.ser = MyClassSerial(pack, pack)
            self.ser.open(timeout=1)

        self.ser_con = PyuiClassFrameSerControl(ser=self.ser)
        self.ser_con.setParent(self)
        self.ser_con.setGeometry(220, 350, 100, 0)

        self.show()
        self.timer_50ms = QTimer(self)
        self.timer_50ms.start(4)
        self.timer_50ms.timeout.connect(self.send_timer)

        self.timer_500ms = QTimer(self)
        self.timer_500ms.start(500)
        self.timer_500ms.timeout.connect(self.task_500ms)

        if self.ser.is_open():
            x = True
            if x is True:
                self.read_bit_tread = MyClassQtTreadReadBit(self.ser)
                self.read_bit_tread.trigger.connect(self.on_ser_read_bit)
                self.read_bit_tread.start()
            else:
                self.read_pack_thread = MyClassQtTreadReadPack(self.ser)
                self.read_pack_thread.trigger.connect(self.on_ser_read_pack)
                self.read_pack_thread.start()

    def on_pushButton_reset_released(self):
        # print('on_pushButton_reset_released')4
        self.joystick = [0,0,0,0, 0,0,0, 0,0]
        self.checkBox_R_down.setChecked(False)
        self.checkBox_L_up.setChecked(False)
        self.checkBox_L_down.setChecked(False)
        self.checkBox_R_up.setChecked(False)
        self.horizontalSlider_L_up.setValue(0)
        self.horizontalSlider_L_down.setValue(0)
        self.horizontalSlider_R.setValue(0)
        self.horizontalSlider_Lx.setValue(0)
        self.horizontalSlider_Ly.setValue(0)
        self.horizontalSlider_Rx.setValue(0)
        self.horizontalSlider_Ry.setValue(0)

        self.label_Lx.setText('0')
        self.label_Ly.setText('0')
        self.label_Rx.setText('0')
        self.label_Ry.setText('0')

        self.label_P_R.setText('0')
        self.label_P_L_up.setText('0')
        self.label_P_L_down.setText('0')

    def on_pushButton_L_down_released(self):
        # print('on_pushButton_L_down_released')
        self.joystick[8] &= ~0x80

    def on_pushButton_L_right_released(self):
        # print('on_pushButton_L_right_released')
        self.joystick[8] &= ~0x40

    def on_pushButton_L_up_released(self):
        # print('on_pushButton_L_up_released')
        self.joystick[8] &= ~0x20

    def on_pushButton_L_left_released(self):
        # print('on_pushButton_L_up_released')
        self.joystick[8] &= ~0x10


    def on_pushButton_R_down_released(self):
        # print('on_pushButton_R_down_released')
        self.joystick[7] &= ~0x08

    def on_pushButton_R_right_released(self):
        # print('on_pushButton_R_right_released')
        self.joystick[7] &= ~0x04

    def on_pushButton_R_up_released(self):
        # print('on_pushButton_R_up_released')
        self.joystick[7] &= ~0x02

    def on_pushButton_R_left_released(self):
        # print('on_pushButton_R_up_released')
        self.joystick[7] &= ~0x01

    def on_pushButton_L_down_pressed(self):
        # print('on_pushButton_L_down_pressed')
        self.joystick[8] |= 0x80

    def on_pushButton_L_right_pressed(self):
        # print('on_pushButton_L_right_pressed')
        self.joystick[8] |= 0x40

    def on_pushButton_L_up_pressed(self):
        # print('on_pushButton_L_up_pressed')
        self.joystick[8] |= 0x20

    def on_pushButton_L_left_pressed(self):
        # print('on_pushButton_L_up_pressed')
        self.joystick[8] |= 0x10

    def on_pushButton_R_down_pressed(self):
        # print('on_pushButton_R_down_pressed')
        self.joystick[7] |= 0x08

    def on_pushButton_R_right_pressed(self):
        # print('on_pushButton_R_right_pressed')
        self.joystick[7] |= 0x04

    def on_pushButton_R_up_pressed(self):
        # print('on_pushButton_R_up_pressed')
        self.joystick[7] |= 0x02

    def on_pushButton_R_left_pressed(self):
        # print('on_pushButton_R_up_pressed')
        self.joystick[7] |= 0x01

    def on_pushButton_W_L_pressed(self):
        # print('on_pushButton_W_L_pressed')
        self.joystick[8] |= 0x08

    def on_pushButton_W_R_pressed(self):
        # print('on_pushButton_W_R_pressed')
        self.joystick[8] |= 0x08

    def on_pushButton_W_L_released(self):
        # print('on_pushButton_W_L_released')
        self.joystick[8] &= ~0x08

    def on_pushButton_W_R_released(self):
        # print('on_pushButton_W_R_released')
        self.joystick[8] &= ~0x08

    def on_checkBox_L_up_released(self):
        # print('on_checkBox_L_up_released')
        if self.checkBox_L_up.isChecked():
            self.joystick[7] |= 0x10
        else:
            self.joystick[7] &= ~0x10

    def on_checkBox_L_down_released(self):
        # print('on_checkBox_L_down_released')
        if self.checkBox_L_down.isChecked():
            self.joystick[7] |= 0x20
        else:
            self.joystick[7] &= ~0x20

    def on_checkBox_R_up_released(self):
        # print('on_checkBox_R_up_released')
        if self.checkBox_R_up.isChecked():
            self.joystick[7] |= 0x40
        else:
            self.joystick[7] &= ~0x40

    def on_checkBox_R_down_released(self):
        # print('on_checkBox_R_down_released')
        if self.checkBox_R_down.isChecked():
            self.joystick[7] |= 0x80
        else:
            self.joystick[7] &= ~0x80

    def on_horizontalSlider_L_down_sliderMoved(self, p_int):
        # print("on_horizontalSlider_L_down_actionTriggered", p_int)
        self.label_P_L_down.setText(str(p_int))
        self.joystick[6] = p_int

    def on_horizontalSlider_L_up_sliderMoved(self, p_int):
        # print("on_horizontalSlider_L_up_actionTriggered", p_int)
        self.label_P_L_up.setText(str(p_int))
        self.joystick[4] = p_int

    def on_horizontalSlider_R_sliderMoved(self, p_int):
        # print("on_horizontalSlider_L_up_actionTriggered", p_int)
        self.label_P_R.setText(str(p_int))
        self.joystick[5] = p_int

    def on_horizontalSlider_Rx_sliderMoved(self, p_int):
        if p_int < self.dead_band and p_int > -self.dead_band:
            p_int = 0
        self.label_Rx.setText(str(p_int))
        self.joystick[0] = p_int

    def on_horizontalSlider_Ry_sliderMoved(self, p_int):
        if p_int < self.dead_band and p_int > -self.dead_band:
            p_int = 0
        self.label_Ry.setText(str(p_int))
        self.joystick[1] = p_int

    def on_horizontalSlider_Lx_sliderMoved(self, p_int):
        if p_int < self.dead_band and p_int > -self.dead_band:
            p_int = 0
        self.label_Lx.setText(str(p_int))
        self.joystick[2] = p_int

    def on_horizontalSlider_Ly_sliderMoved(self, p_int):
        if p_int < self.dead_band and p_int > -self.dead_band:
            p_int = 0
        self.label_Ly.setText(str(p_int))
        self.joystick[3] = p_int

    def send_timer(self):
        self.label_mode.setText(hex(self.joystick[7] & 0xf0))
        if self.ser.is_open() is True:
            pack = self.ser.class_pack.pack(*self.joystick)
            self.ser.write_pack(pack)
            # print(pack)
        else:
            # self.close()
            pass

    def task_500ms(self):
        pass

    def on_ser_read_bit(self, bits:'bytes'):
        # print('on_ser_read_bit')
        print(bits.decode(), end='')
        pass

    def on_ser_read_pack(self, pack:'bytes'):
        # print('on_ser_read_pack')
        pack = self.ser.class_unpack.unpack(pack)
        print(pack)


if __name__ == '__main__':
    plt.ion()
    app = QApplication(sys.argv)
    pyui = PyuiClassFrameJoystick(show=True)
    sys.exit(app.exec())

