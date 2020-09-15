# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer, QThread, pyqtSignal
from PyQt5.QtWidgets import QMainWindow
import time

from MyClass import MyClassSerial
# from MyClass import MyClassPack
# from MyClass import MyClassPlot
# import matplotlib.pyplot as plt


class MyClassQtTreadReadPack(QThread):

    trigger = pyqtSignal(bytes)

    def __init__(self, ser:'MyClassSerial'):
        super(MyClassQtTreadReadPack, self).__init__()
        if isinstance(ser, MyClassSerial):
            self.ser_thread = ser
        else:
            self.ser_thread = MyClassSerial()
        print('MyClassQtTreadReadPack init')

    def run(self):
        while True:
            pack = self.ser_thread.read_pack()
            if pack is None:
                pass
            else:
                self.trigger.emit(pack)


class MyClassQtTreadReadLine(QThread):

    trigger = pyqtSignal(str)

    def __init__(self, ser:'MyClassSerial' = None):
        super(MyClassQtTreadReadLine, self).__init__()
        if isinstance(ser, MyClassSerial):
            self.ser_thread = ser
        else:
            self.ser_thread = MyClassSerial()

        print('MyClassQtTreadReadLine init')

    def run(self):
        while True:
            rec_str = self.ser_thread.read_line()
            if rec_str is None:
                pass
            else:
                self.trigger.emit(rec_str)


class MyClassQtTreadReadBit(QThread):

    trigger = pyqtSignal(bytes)
    def __init__(self, ser:'MyClassSerial'):
        super(MyClassQtTreadReadBit, self).__init__()
        if isinstance(ser, MyClassSerial):
            self.ser_thread = ser
        else:
            self.ser_thread = MyClassSerial()
        print('MyClassQtTreadReadBit init')

    def run(self):
        while True:
            bits = self.ser_thread.read_bit()
            if bits is None:
                pass
            else:
                self.trigger.emit(bits)


if __name__ == '__main__':

    class UI_My_MainWindow(QMainWindow):
        def __init__(self):
            super(UI_My_MainWindow, self).__init__()
            self.show()

        def task_my_thread(self, par):
            print(par)

    app = QApplication(sys.argv)
    test = UI_My_MainWindow()
    sys.exit(app.exec())







