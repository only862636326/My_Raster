# -*- coding: UTF-8 -*-

import serial
import serial.tools.list_ports as l_ports
import threading
import time
from MyClass.MyClassPackFile import MyClassPack
import numpy as np


class MyClassSerial(object):
    """
    串口的简单封装
    """
    ARRAY_NUM = 100
    MAX_PACK_NUM = 2

    def __init__(self, c_pack1: 'MyClassPack' = None, c_pack2: 'MyClassPack' = None):
        """
        :param c_pack1: 一个数据打包的对象， 用于串口数据打包
        :param c_pack2: 一个数据打包的对象， 用于串口数据解包

        当参数c_pack2 不存在时 解包和打包数据格式一样
        用两个数据打包对象，以实现打包数据和解包数据格式不同

        self.ser
        self.ser_threads
        self.packs
        self.array
        self.class_pack
        self.class_unpack

        """
        self.ser = serial.Serial()
        self.ser_threads = []
        self.packs = []

        if isinstance(c_pack1, MyClassPack):
            # 打包对象
            self.class_pack = c_pack1
        else:
            self.class_pack = MyClassPack()

        if c_pack2 is not None:
            # 解包对象
            if isinstance(c_pack2, MyClassPack):
                self.class_unpack = c_pack2
            else:
                self.class_pack = MyClassPack()
        else:
            self.class_unpack = self.class_pack
            # self.class_unpack = MyClassPack(*self.class_pack.get_pack_info())

        self.array = np.zeros((self.ARRAY_NUM, self.class_unpack.data_len), dtype=np.float32)
        print('ser Init')

    def show_ser_info(self):
        print('打包信息', self.class_pack.get_pack_info())
        print('解包信息', self.class_unpack.get_pack_info())
        print('串口信息', self.ser)

    def get_use_com_name(self):
        return self.ser.name

    def is_use_com_exist(self):
        """

        :return: True : 存在
                 False: 在存在
                 None : 串口未设定
        """
        coms = self.get_all_com()
        use_com = self.get_use_com_name()
        # print(com)
        if use_com is None:
            return None
        elif use_com in coms:
            return True
        else:
            return False

    def change_pack(self,  c_pack:'MyClassPack'):
        if isinstance(c_pack, MyClassPack):
            self.class_pack = c_pack
            return True
        else:
            return False

    def change_unpack(self, c_unpack: 'MyClassPack'):
        if isinstance(c_unpack, MyClassPack):
            self.class_unpack = c_unpack
            self.array = np.zeros((self.ARRAY_NUM, self.class_unpack.data_len), dtype=np.float32)
            return True
        else:
            return False

    def is_open(self):
        return self.ser.is_open

    @staticmethod
    def get_all_com():
        """
        获取当前电脑所有串口
        :return:
        """
        ports_str = []
        ports = l_ports.comports()
        for port in ports:
            ports_str.insert(0, port.device)
        return ports_str

    def open(self, com:'str' = None, bound:'int' = 115200, timeout = None):
        """
        打开串口,
        打开之后才能使用
        :param bound:
        :return:1, Ture, False
                2, 错误原因
        """
        if com is None:
            ports = self.get_all_com()
            if len(ports) == 0:
                print("No COM")
                return False, "No COM"
            else:
                for port in ports:
                    try:
                        self.ser = serial.Serial(port, bound, timeout=timeout)
                        print('打开串口成功： ', self.ser)
                        return True, port
                    except:
                        print(port + "被占用")

                print("无空闲串口")
                return False, "无空闲串口"
        else:
            com = com.upper()
            ports = self.get_all_com()
            if com in ports:
                try:
                    self.ser = serial.Serial(com, bound, timeout=timeout)
                    print('打开串口成功： ', self.ser)
                    return True, com
                except :
                    print(com, '被占用')
                    return False, com + '被占用'
            else:
                print(com, '不存在')
                return False, com + '不存在'

    def close(self):
        self.ser.close()

    def read_bit(self, size = 1):
        """
        从串口中读取size大小的数据
        :param size:
        :return:
        """
        try :
            data = self.ser.read(size)
            return data
        except:
            time.sleep(0.1)
            return None

    def read_line(self):
        """
        读取一行数据， \n 为止
        :return: 数据字符串
        """
        try:
            return self.ser.readline().decode()
        except:
            time.sleep(0.02)
            return None

    def read_pack(self):
        '''
        根据设置的格式从串口读取一个数据包,
        :return:  :帧错误返回 None
                  :帧正确返回 一个数据包
        '''

        for i in range(10):
            data = self.read_bit(1)
            if data == self.class_unpack.frame_head: #等待帧头1出现
                break
            if i == 9:
                return None

        if self.class_unpack.frame_head2 != b'': #存在帧头2
            data = self.read_bit(1)
            if data == self.class_unpack.frame_head:# 把帖尾判断为帖头时
                data = self.read_bit(1)
            if data != self.class_unpack.frame_head2: # 帧头2错误 直接返回
                return None
        # 接收数据
        data_pack = self.read_bit(self.class_unpack.Struct.size)

        # 帧尾判断
        if self.read_bit(1) == self.class_unpack.frame_end:
            if self.class_unpack.frame_end2 != b'':#存在帧尾2
                if self.read_bit(1) == self.class_unpack.frame_end2:
                    return data_pack
                else:
                    return None
            else:#不存在帧尾2
                return data_pack
        else:#帧尾1 错误
            return None

    def write_bits(self, bits):
        '''
        写bit
        :param bits: bits 数据串
        :return:
                True:写入成功
                False:写入失败
        '''
        try :
            self.ser.write(bits)
            return True
        except:
            return False

    def write_pack(self, pack):
        '''
        写一个数据包
        :param pack: 数据包
        :return:
                True:写入成功
                False:写入失败
        '''
        return self.write_bits(pack)

    def write_str(self, data: 'str'):
        """
        写字符串
        :param data:字符串
        :return: True:写入成功
                 False:写入失败
        """
        return self.write_bits(data.encode())

    def read_threading(self):
        """
        一个读取数据的死循环,用于测试
        :return:
        """
        pass

    def write_threading(self):
        """
        一个写数据的死循环, 用于测试
        :param data:
        :return: 无
        """
        # # class_pack = My_Class_Pack(r'ff', b'\x0D', b'\x0A', b'\x0A', b'\x0D')
        pass

    def plot_threading(self):
        """
        plot
        :return:
        """
        pass

    def run(self):
        print('ser_run')
        self.ser_threads.append(threading.Thread(target=self.write_threading, name='write_bit', ))
        self.ser_threads.append(threading.Thread(target=self.read_threading, name='write_bit', ))
        self.ser_threads.append(threading.Thread(target=self.plot_threading, name='plot', ))
        self.ser_threads[0].start()
        self.ser_threads[1].start()
        self.ser_threads[2].start()
        # self.ser_threads[3].start()
        print('ser_end')

    def __del__(self):
        self.ser.close()

if __name__ == '__main__':
    my_pack = MyClassPack(r'=hhhhhhhBB', b'\xAA', b'\x55', b'\x55', b'\xAA')
    my_serial = MyClassSerial(my_pack, my_pack)
    my_serial.open(bound=12341300)
    # my_serial.run()
    print(my_serial.get_all_com())













