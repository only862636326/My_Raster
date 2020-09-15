# -*- coding: UTF-8 -*-

from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import time


class MyClassPlot(object):


    def __init__(self, num = 4):
        # self.fig_ = Figure()
        self.fig = plt.figure()
        self.axis = []

        #
        self.axis.append(self.fig.add_subplot(121))
        self.axis.append(self.fig.add_subplot(122))

        self.add_axis()
        self.fig.show()


    def thread_plot(self, pasuse_time = 1):
        while True:
            # self.i.append(len(self.i)**2)
            # print(self.i)
            # self.axis[0].plot(self.i, color = 'red')
            # self.axis[1].plot(self.i, color = 'red')
            plt.pause(1)

    def pause(self, pause_time = 1):
        plt.pause(pause_time)
        self.fig.show()

    def plot_xy(self, x, y, color = 'red', cla = False):
        if cla is True:
            self.axis[0].cla()
        self.axis[0].plot(x, y)

    def plot(self, data, num=0):
        self.axis[num].plot(data)
        self.fig.show()
        # plt.show()

    def add_axis(self, num = 0):
        self.fig.clf()
        if num == 1 or num == 0:
            self.axis.append(self.fig.add_subplot())
        elif num == 2:
            self.axis.append(self.fig.add_subplot(121))
            self.axis.append(self.fig.add_subplot(122))
        elif num == 4:
            self.axis.append(self.fig.add_subplot(221))
            self.axis.append(self.fig.add_subplot(222))
            self.axis.append(self.fig.add_subplot(223))
            self.axis.append(self.fig.add_subplot(224))


if __name__ == '__main__':

    a = MyClassPlot()
    a.plot([123,123,31,123,12,31,3,12])
    a.thread_plot()


















