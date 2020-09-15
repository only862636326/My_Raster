import sys
from PyQt5.QtWidgets import QFrame, QMainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer, pyqtBoundSignal

from PyuiPlot.PlotCanvas import PlotCanvas
from PyuiPlot.UI_Setup_Frame_PlotCanvas import Ui_Frame_PlotCanvas
import matplotlib.pyplot as plt

class UI_Class_PlotCanvas(QFrame, Ui_Frame_PlotCanvas):

    def __init__(self, parent = None, pushButton = None, num=1):
        super(UI_Class_PlotCanvas, self).__init__()
        self.setupUi(self)
        self.plotCanvas = PlotCanvas()
        self.gridLayout.addWidget(self.plotCanvas)
        self.axes = []
        self.axes_num = 0
        self.set_num(num)
        self.show()

        # 200 ms 自动刷新一次图象
        self.time = QTimer(self)
        self.time.start(200)
        self.time.timeout.connect(self.freshen)

        # self.time2 = QTimer(self)
        # self.time.start(1000)
        # self.time.timeout.connect(self.change_num_test)

    def set_num(self, num = 1, *axes_names):
        """
        设置子图的数据, 只能为1, 2, 3, 4
        :param num:子图数量
        :param axes_names:子图名
        :return:
        """
        if num in range(1, 5):
            self.plotCanvas.fig.clf()
            self.axes = []
            self.axes_num = num
        else:
            print('set num err')
            return

        if num == 4:
            self.axes.append(self.plotCanvas.fig.add_subplot(221))
            self.axes.append(self.plotCanvas.fig.add_subplot(222))
            self.axes.append(self.plotCanvas.fig.add_subplot(223))
            self.axes.append(self.plotCanvas.fig.add_subplot(224))
        elif num == 1:
            self.axes.append(self.plotCanvas.fig.add_subplot(111))
        elif num == 2:
            self.axes.append(self.plotCanvas.fig.add_subplot(211))
            self.axes.append(self.plotCanvas.fig.add_subplot(212))
        elif num == 3:
            self.axes.append(self.plotCanvas.fig.add_subplot(131))
            self.axes.append(self.plotCanvas.fig.add_subplot(132))
            self.axes.append(self.plotCanvas.fig.add_subplot(133))
        self.set_title(axes_names)

        for i in self.axes:
            i.grid()

    def my_plot(self, data=None, num=0, cla=True, *args, **kwargs):
        """
        画图
        数据优先级依次升高
        :param data: 要画的数据
        :param cla: 是否清除上次数据
        :param args: 要画的数据集
        :param kwargs: 数据字典
        :return:
        """
        args_len = len(args)
        kwargs_len = len(kwargs)
        # 字典, 列表都为空
        if kwargs_len == 0 and args_len == 0:
            try:
                if cla is True:
                    self.axes[num].cla()
                self.axes[num].grid()
                self.axes[num].plot(data)
            except:
                print('data err')
        # 字典的数据
        elif kwargs_len < self.axes_num:
            for key, value in kwargs.items():
                try:
                    key = key[len(key) - 1]
                    key = int(key)
                except ValueError:
                    print('plot key err')

                try:
                    self.axes[key].cla()
                    self.axes[key].plot(value)
                    self.axes[key].grid()
                except:
                    print('plot data err')

        elif args_len < self.axes_num:
            for i in range(args_len):
                print(i)
                if cla is True:
                    self.axes[i].cla()
                try:
                    self.axes[i].plot(args[i])
                    self.axes[i].grid()
                except:
                    print('plot data err')

    def my_plot_xy(self, data_x, data_y, cla=False, color=None):
        if cla is True:
            self.axes[0].cla()
            self.axes[0].grid()
        self.axes[0].plot(data_x, data_y, color=color)

    def freshen(self):
        """
        画面刷新函数, 定时器周期调用
        :return:
        """
        self.plotCanvas.draw()

    def change_num_test(self):
        '''
        用于测试改变窗口数量
        :return:
        '''
        self.axes_num += 1
        if self.axes_num == 5:
            self.axes_num = 1
        self.set_num(self.axes_num)

    def set_title(self, *args, **kwargs):
        """
        设置子图的标题
        字曲优先
        :param args:
        :param kwargs:标题,字典, key最后的数为子图号, 0开始
        :return:
        """
        if len(kwargs) in range(1, self.axes_num+1):
            for key, value in kwargs.items():
                try:
                    key = key[len(key)-1]
                    key = int(key)
                except ValueError:
                    print('title key err')
                else:
                    self.axes[key].set_title(str(value))

        elif len(args) in range(1, self.axes_num+1):
            if isinstance(args[0], (tuple, list)) is True:
                args = args[0]

                for i in range(len(args)):
                    self.axes[i].set_title(str(args[i]))
        else:
            print("input param err")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    plotCanvas = UI_Class_PlotCanvas(num=1)
    plotCanvas.my_plot_xy([12,13,123,2,1], [1231,3,234,523,4],color="RED")
    sys.exit(app.exec())













