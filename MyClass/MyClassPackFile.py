# -*- coding: UTF-8 -*-

from struct import Struct
from struct import error as StructError


class MyClassPack(object):
    """
    数据打包的简单封装
    """
    def __init__(self, fmt='ffffB', frame_head=b'\x0D',frame_head2=b'\x0A',
                                    frame_end=b'\x0A', frame_end2=b'\x0D', name = "pack"):
        """
        :param fmt: 打包格式字符串

                            > 大端        < 小端     = 字节对齐
                    c char  b: int8_t      B: uint8_t
                            h: int16_t     H: uint16_t
                            i: int         I: unsigned int
                            f: float       d: double

        :param frame_head:   帧头1
        :param frame_end:    帧尾1
        :param frame_head2:  帧头2   没有则不设置
        :param frame_end2:   帧尾2   没有则不设置
        """

        self.frame_head = frame_head
        self.frame_end = frame_end
        self.frame_head2 = frame_head2
        self.frame_end2 = frame_end2
        self.name = name

        try:
            self.Struct = Struct(fmt)
        except:
            print('init fmt err')
            self.Struct = Struct('ffffB')
            fmt = 'ffffB'

        if fmt[0] == '>' or fmt[0] == '<' or fmt[0] == '=':
            self.data_len = len(fmt) - 1
        else:
            self.data_len = len(fmt)

    def pack(self, *args):
        """
        数据打包， 打包成对象的格式
        :param args: 要打包的数据
        :return: 打包 成功则返回 打包的二进制串
                      失败则返回 None
        """
        if self.data_len != len(args):
            print('pack data len err')
            return None
        try:
            data = self.Struct.pack(*args)
        except:
            print('pack data type err ')
            return None
        ser_pack = self.frame_head + self.frame_head2 + data + self.frame_end + self.frame_end2
        return ser_pack

    def unpack(self, buff):
        """
        数据解包， 把对应的buff中的数据解包成数据
        不带帖头帖尾
        :param buff: 数据包二进制串
        :return: 解包 成功 返回 数据元组
                      失败 返回 None
        """
        try:
            data = self.Struct.unpack(buff)
            return data
        except:
            # print('unpack data err')
            return None

    def get_pack_info(self):
        """
        :return:
        """
        return self.Struct.format, \
                self.frame_head, self.frame_head2, \
                self.frame_end, self.frame_end2, self.name

    @staticmethod
    def str2bytes(x: 'str'):
        x = x.upper()
        if len(x) > 2 and x[0] == '0' and x[1] == 'X':
            x = x[2:]
        if x == '0X':
            return b''
        try:
            b = bytes.fromhex(x)
        except:
            b = None
        return b

    def get_dict(self):
        info = {}
        info['fmt'] = self.Struct.format
        info['head1'] = '0x' + self.frame_head.hex()

        if self.frame_head2 is not None:
            info['head2'] = '0x' + self.frame_head2.hex()
        else:
            info['head2'] = 'None'
        if self.frame_end is not None:
            info['end1'] = '0x' + self.frame_end.hex()
        else:
            info['end1'] = 'None'
        info['end2'] = '0x' + self.frame_end2.hex()
        info['name'] = self.name
        return info

    @staticmethod
    def dic2p(info:'dict'):
        """
        返回创建对应的参数
        :param dic:
        :return:
        """
        # for k, info in d.items():
        fmt = info['fmt']
        head1 = MyClassPack.str2bytes(info['head1'])
        if info['head2'] == 'None':
            head2 = b''
        else:
            head2 = MyClassPack.str2bytes(info['head2'])
        if info['end1'] == 'None':
            end1 =  b''
        else:
            end1 = MyClassPack.str2bytes(info['end1'])
        end2 = MyClassPack.str2bytes(info['end2'])
        name = info['name']
        return fmt, head1, head2, end1, end2, name


if __name__ == '__main__':
    my_pack = MyClassPack(r'=hhhBB', b'\xAA', b'0x23', b'', b'')
    # pack = my_pack.pack(257,3,3,3, 3,3,3, 3,3)
    # print(type(pack))
    # s = my_pack.get_dict()
    # b = my_pack.dic2p(s)
    print(MyClassPack.str2bytes('0x'))









