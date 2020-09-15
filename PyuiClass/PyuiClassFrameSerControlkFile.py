# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QFrame
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer, Qt

from MyClass import MyClassSerial
from PyuiClass.PyuiSetupFrameSerControl import Ui_FrameSerControl

class PyuiClassFrameSerControl(QFrame, Ui_FrameSerControl):
    """

    """
    def __init__(self, ser:'MyClassSerial' = None, show = False):
        super(PyuiClassFrameSerControl, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowMinimizeButtonHint|Qt.WindowCloseButtonHint)
        self.setFixedSize(self.width(), self.height())
        self.comboBox_com_choose.clear()

        if isinstance(ser, MyClassSerial):
            self.use_com = ser
            if self.use_com.is_open() is True:
                self.pushButton_open.hide()
            else:
                self.pushButton_close.hide()

        else:
            self.use_com = MyClassSerial()
            self.com_show_init()
            # self.use_com.open()
        if show is True:
            self.show()
        self.timer_500ms = QTimer(self)
        self.timer_500ms.start(500)
        self.timer_500ms.timeout.connect(self.com_check)

    def com_show_init(self):
        """
        串口显示初始化
        获取电脑所有串口并显示出来

        当没有串口时隐藏打开按键
        :return:
        """
        self.comboBox_com_choose.clear()
        coms = MyClassSerial.get_all_com()

        self.pushButton_close.hide()
        self.pushButton_open.hide()
        if len(coms) == 0:
            self.label_ser_info.setText('')
        else:
            for com in coms:
                self.comboBox_com_choose.insertItem(0, com)
            self.comboBox_com_choose.setCurrentIndex(0)
            self.pushButton_close.hide()
            self.pushButton_open.show()
        # self.label_ser_info.setText('')

    def on_pushButton_open_released(self):
        """
        打开combox中的串口
        若打开失败在label_ser_info中显示错误原因
        :return:
        """
        print('on_pushButton_open_released')
        com_name = self.comboBox_com_choose.currentText()
        if com_name =='':
            pass
        else:
            flag, reason = self.use_com.open(com_name)
            print(self.use_com)
            if flag is True:
                self.pushButton_open.hide()
                self.pushButton_close.show()
            else:
                self.label_ser_info.setText(reason)

    def on_comboBox_com_choose_activated(self, p_str):
        print('on_comboBox_com_choose_activated', p_str)
        if isinstance(p_str, int):
            return
        if self.use_com.get_use_com_name() == self.comboBox_com_choose.currentText():
            if self.use_com.is_open() is True:
                pass
            else:
                self.on_pushButton_open_released()
        else:
            self.use_com.ser.close()
            self.on_pushButton_open_released()

    def on_pushButton_close_released(self):
        print('on_pushButton_close_released')
        self.use_com.close()
        self.com_show_init()

    def com_check(self):
        """
        周期性检查当前的串口状态

        :return:
        """
        # print('com_check')
        # print('com_check_1000ms')
        sta = self.use_com.is_use_com_exist()
        if sta is None:
            self.com_show_init()
            pass
        elif sta is True:
            # 存在
            if self.use_com.is_open() is True:
                self.label_ser_info.setText('串口{}使用中'.format(self.use_com.get_use_com_name()))

            else:
                self.label_ser_info.setText('')
        else:
            self.com_show_init()
            self.use_com.ser.name = None


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ser = MyClassSerial()
    pyui = PyuiClassFrameSerControl(ser=ser, show=True)
    sys.exit(app.exec())

