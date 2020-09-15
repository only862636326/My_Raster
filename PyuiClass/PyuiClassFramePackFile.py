# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QFrame
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer, Qt

from MyClass import MyClassSerial, MyClassPack, MyClassQtTreadReadBit, MyClassQtTreadReadPack, MyClassQtTreadReadLine
from PyuiClass.PyuiSetupFramePack import Ui_FramePack
from PyuiClass import PyuiClassFrameSerControl, PyuiClassFramePackInfo
from PyuiPlot.UI_Class_PlotCanvas import UI_Class_PlotCanvas
from UiMyBase.UiClassMyBase import UiClassMyBase

import matplotlib.pyplot as plt
import numpy as np


class PyuiClassFramePack(QFrame,Ui_FramePack):

    def __init__(self, ser:'MyClassSerial' = None, show = False):
        super(PyuiClassFramePack, self).__init__()
        self.setupUi(self)


        # 串口
        if ser is not None:
            self.ser = ser
        else:
            self.ser = MyClassSerial()

        self.x = 0
        self.y = 0

        # com
        self.ser_con = PyuiClassFrameSerControl(ser=self.ser)
        self.gridLayout_3.addWidget(self.ser_con)

        # 画布
        self.plotCanvas = UI_Class_PlotCanvas(num=1)
        self.plotCanvas.hide()


        self.pack_control = PyuiClassFramePackInfo(ser=self.ser)

        # self.ser_read_thread = MyClassQtTreadReadPack(self.ser)
        # self.ser_read_thread.trigger.connect(self.on_ser_read_pack_finish)
        # self.ser_read_thread.start()

        # 成员变量
        self.cashe = 100
        self.data_len = self.ser.class_unpack.data_len
        self.recive_num = 0
        self.table_show_where = 0
        self.is_data_show = True
        self.array = np.zeros((self.cashe, self.data_len), dtype=np.float32)


        # self.timer = QTimer(self)
        # self.timer.start(100)
        # self.timer.timeout.connect(self.rand_data)

        self.timer = QTimer(self)
        self.timer.start(500)
        self.timer.timeout.connect(self.show_in_table)

        if show is True:
            self.show()

        # 弹窗
        self.dialog = UiClassMyBase()
        self.dialog.trigger.connect(self.yes_no)

    def yes_no(self, sig):
        # print(sig)
        pass

    def show_in_table(self):
        if self.recive_num == 0:
            pass
        elif self.is_data_show is not True:
            for j in range(self.data_len):
                self.tableWidget.setItem(self.table_show_where, j,
                                         QTableWidgetItem(str(self.array[-1, j])))
                self.tableWidget.setItem(self.table_show_where+1, j,
                                         QTableWidgetItem(' '))
            self.table_show_where += 1
            if self.table_show_where >= 20:
                self.table_show_where = 0
            self.is_data_show = True

    def random_data(self):
        data = np.random.random(self.data_len)
        pack = self.ser.class_pack.pack(*data)
        pack = pack[2:-2]
        self.on_ser_read_pack_finish(pack)

    def on_ser_read_pack_finish(self, pack):
        # print(pack)
        datas = self.ser.class_pack.unpack(pack)
        self.array[:] = np.vstack((self.array[1:], datas))[:]
        self.is_data_show = False
        self.recive_num = self.recive_num + 1
        if self.recive_num > self.cashe:
            self.recive_num = self.cashe
        else:
            self.label_data_num.setText(str(self.recive_num) + r'/' + str(self.cashe))

        if self.recive_num > self.cashe:
            self.recive_num = self.cashe
        self.label_data_num.setText(str(self.recive_num) + r'/' + str(self.cashe))

    def on_pushButton_draw_x_released(self):
        # print('on_pushButton_drawx_released')
        text = self.label_x_value.text()
        if text == '':
            pass
        else:
            c = int(text) - 1
            self.plotCanvas.my_plot(self.array[:,c])
            self.plotCanvas.show()

    def on_pushButton_draw_xy_released(self):
        # print('on_pushButton_drawxy_released')
        text_x = self.label_x_value.text()
        text_y = self.label_y_value.text()
        if text_x == '' or text_y == '':
            pass
        else:
            c = int(text_x) - 1
            r = int(text_y) - 1
            self.plotCanvas.my_plot_xy(self.array[-self.recive_num:, c], self.array[-self.recive_num:,r], cla=True)
            self.plotCanvas.show()

    def on_pushButton_data_save_released(self):
        # print('on_pushButton_data_save_released')
        file_name = 'packs'
        file_num = 1
        file_type = '.csv'
        np.savetxt('packs.csv', self.array, "%.5f", ',')
        self.dialog.my_dialog_msg('保存成功')

    def on_pushButton_data_clear_released(self):
        # print('on_pushButton_data_clear_released')
        self.array.fill(0)
        self.recive_num = 0
        self.table_show_where = 0
        self.tableWidget.clearContents()

    def on_tableWidget_itemSelectionChanged(self):
        n = self.tableWidget.currentColumn() + 1
        if n > self.data_len:
            pass
        else:
            self.label_y_value.setText(self.label_x_value.text())
            self.label_x_value.setText(str(n))

    def on_pushButton_send_released(self):
        fmt = self.ser.class_pack.Struct.format
        datas = []
        while fmt[0] in ['>', '<', '=']:
            fmt = fmt[1:]

        for i in range(self.ser.class_pack.data_len):
            item = self.tableWidget_2.item(self.tableWidget_2.currentRow(), i)
            if item is not None:
                if fmt[i] in ['f', 'd']:
                    try:
                        data = float(item.data(0))
                        datas.append(data)
                    except:
                        break
                elif fmt[i] in "bBiIhH":
                    try:
                        data = int(item.data(0))
                        datas.append(data)
                    except:
                        break
            else:
                break
        if len(datas) == self.ser.class_pack.data_len:
            pack = self.ser.class_pack.pack(*datas)
            # print(pack)
            # self.on_ser_read_pack_finish(pack[2:-2])
        else:
            self.dialog.my_dialog_msg('输入格式错误')

    def on_pushButton_pack_set_released(self):
        # print('on_pushButton_pack_set_released')
        self.pack_control.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    pyui = PyuiClassFramePack(show=True)
    sys.exit(app.exec())

