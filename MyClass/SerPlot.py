# -*- coding: utf-8 -*-

import time
import random
import numpy as np
import matplotlib.pyplot as plt
from MyClass import MyClassPack
from MyClass import MyClassSerial

class SerRecivePlot(MyClassSerial):

    def __init__(self, c_pack1: 'MyClassPack' = None, c_pack2: 'MyClassPack' = None):
        super(SerRecivePlot, self).__init__(c_pack1, c_pack2)
        self.write_stop_time = 0.01
        self.plt_stop_time   = 0.1
        self.recive_num = 1

    def read_threading(self):
        while True:
            pack = self.read_pack()
            if pack is not None:
                datas = self.class_unpack.unpack(pack)
                self.packs.append(datas)
                print(datas)
                self.array[:] = np.vstack((self.array[1:], datas))[:]
                self.recive_num = self.recive_num + 1
                # print(ser.array[-1])

    def write_threading(self):

        while True:
            a1 = random.randrange(0, 100)
            a2 = random.randrange(0, 100)
            a3 = random.randrange(0, 100)
            a4 = random.randrange(0, 100)
            a5 = random.randrange(0, 100)

            pack = ser.class_pack.pack(a1, a2, a3, a4, a5)

            self.write_pack(pack)
            time.sleep(self.write_stop_time)


    def plot_threading(self):

        fig1 = plt.figure(0)
        axis1 = fig1.add_axes((0.05, 0.08, 0.6, 0.85))
        axis2 = fig1.add_axes((0.70, 0.18, 0.25, 0.32))
        axis3 = fig1.add_axes((0.70, 0.58, 0.25, 0.32))

        # fig2 = plt.figure(1)
        # axis21 = fig2.add_subplot(211)
        # axis22 = fig2.add_subplot(212)
        while True:
            try:
                axis1.plot(self.array[-self.recive_num:,0], self.array[-self.recive_num:,1], color = "red")
                self.recive_num = 1

                axis2.cla()
                axis3.cla()
                axis2.plot(self.array[:,1])
                axis3.plot(self.array[:,2])

            except:
                # del(self)
                pass

            plt.pause(self.plt_stop_time)


if __name__ == '__main__':
    plt.ion()
    # a = input()
    pack = MyClassPack(r'=ffffb', b'\x0D', b'\x0A', b'\x0A', b'\x0D')
    ser = SerRecivePlot(pack, pack)
    ser.open()
    ser.run()
    plt.show()