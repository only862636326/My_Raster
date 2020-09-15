import sys
from PyQt5.QtWidgets import QFrame, QMainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer

from PyuiPlot.UI_Class_PlotCanvas import UI_Class_PlotCanvas
from PyuiPlot.UI_Setup_Frame_PlotCanvas import Ui_Frame_PlotCanvas
from MyClass import MyClassSerial, MyClassQtTreadReadPack, MyClassPack

import numpy as np


class UI_Class_RecivePlot(QFrame, Ui_Frame_PlotCanvas):

    def __init__(self, parent = None, pushButton = None, num=4, ser:'MyClassSerial' = None):

        super(UI_Class_RecivePlot,self).__init__()
        self.plot_canvas = []
        self.plot_canvas.append(UI_Class_PlotCanvas(num=1))
        self.plot_canvas.append(UI_Class_PlotCanvas(num=2))
        self.pause_flag = False
        self.plot_point_num = 100
        self.setupUi(self)
        self.gridLayout.addWidget(self.plot_canvas[0], 0, 0, 1, 1)
        self.gridLayout.addWidget(self.plot_canvas[1], 0, 1, 1, 1)
        self.show()

        pack = MyClassPack(r'ffff', b'\x0D', b'\x0B', b'\x0B', b'\x0D')

        if isinstance(ser, MyClassSerial):
            self.ser = ser
            # self.ser.class_unpack = pack
        else:
            self.ser = MyClassSerial(pack, pack)
            flag, info = self.ser.open()
            if flag:

                # 串口定时发送
                self.timer = QTimer(self)
                self.timer.start(100)
                self.timer.timeout.connect(self.ser_send)

        self.ser_read_thread = MyClassQtTreadReadPack(self.ser)
        self.ser_read_thread.trigger.connect(self.on_ser_read_pack_finish)
        self.ser_read_thread.start()
        self.clear_plot()

    def on_ser_read_pack_finish(self, pack):
        print('on_ser_read_pack_finish')
        data = self.ser.class_unpack.unpack(pack)
        # print(data)

        data = np.array(data)
        self.ser.array = np.vstack((self.ser.array[1:], data))

        if self.pause_flag is not True:
            self.plot_canvas[0].my_plot_xy(self.ser.array[self.ser.ARRAY_NUM - 5:, 0], self.ser.array[self.ser.ARRAY_NUM - 5:,1], cla=True,color="RED")
            self.plot_canvas[1].my_plot(self.ser.array[self.ser.ARRAY_NUM - self.plot_point_num:, 2], 0)
            self.plot_canvas[1].my_plot(self.ser.array[self.ser.ARRAY_NUM - self.plot_point_num:, 3], 1)

    def start_thread(self):
        self.ser_read_thread.start()

    def exit_thread(self):
        self.ser_read_thread.sleep()

    def ser_send(self):
        a = np.random.randint(0, 1000)
        b = np.random.randint(0, 1000)
        c = np.random.randint(0, 1000)
        d = np.random.randint(0, 1000)

        pack = self.ser.class_pack.pack(a, b, c, d)
        self.ser.write_pack(pack)

    def clear_plot(self):
        self.plot_canvas[0].my_plot_xy(0, 0, cla=True)
        self.ser.array[:,:] = 0

    def plot_base_map(self, x, y):
        self.plot_canvas[0].my_plot_xy(x, y, cla=True)

    def pause(self):
        self.pause_flag = True

    def continue_plot(self):
        self.pause_flag = False



if __name__ == '__main__':

    app = QApplication(sys.argv)
    x = UI_Class_RecivePlot()
    sys.exit(app.exec())



