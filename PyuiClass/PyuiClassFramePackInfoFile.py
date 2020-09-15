# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QFrame
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer, Qt

from MyClass import MyClassPack, MyClassSerial
from PyuiClass.PyuiSetupFramePackInfo import Ui_Frame_FramInfo
from UiMyBase.UiClassMyBase import UiClassMyBase


import matplotlib.pyplot as plt
# import numpy as np

class PyuiClassFramePackInfo(QFrame, Ui_Frame_FramInfo):

    def __init__(self, ser:'MyClassSerial' = None, set = 'all', show = False, ):
        super(PyuiClassFramePackInfo, self).__init__()
        self.setupUi(self)

        # print(type(self.pack_history))
        # 弹窗
        self.msg_box = UiClassMyBase()
        self.msg_box.trigger.connect(self.yes_no_deal)

        if ser is not None:
            self.ser = ser
        else:
            self.ser = MyClassSerial()

        self.pack_history = {}
        self.load_history()

        if show is True:
            self.show()

    def load_history(self):
        # file
        import json
        try:
            with open('pack_info.json', 'r') as f:
                self.pack_history = json.load(f)

        except FileNotFoundError:
            with open('pack_info.json', 'w') as f:
                self.pack_history = {}
                json.dump(self.pack_history, f)

        self.comboBox.clear()
        for k, v in self.pack_history.items():
            self.comboBox.insertItem(0, k)
        self.comboBox.insertItem(0, '解包')
        self.comboBox.insertItem(0, '打包')
        self.comboBox.insertItem(0, '')
        self.comboBox.setCurrentIndex(1)
        self.show_pack_info(self.ser.class_pack)

    def on_comboBox_activated(self, s):
        # print(s)
        if isinstance(s, int):
            return
        if self.comboBox.currentText() == '':
            self.widget.setEnabled(True)
        elif self.comboBox.currentText() == '解包':
            self.show_pack_info(self.ser.class_unpack)
            self.widget.setEnabled(False)
        elif self.comboBox.currentText() == '打包':
            self.show_pack_info(self.ser.class_pack)
            self.widget.setEnabled(False)
        else:
            name = self.comboBox.currentText()
            d = self.pack_history[name]
            p = MyClassPack.dic2p(d)
            c_pack = MyClassPack(*p)
            self.show_pack_info(c_pack)
            self.widget.setEnabled(True)

    def yes_no_deal(self, sig):

        print(sig)

    def show_pack_info(self, c_pack:'MyClassPack'):
        # print(packInfo)
        self.lineEdit_name.setText(c_pack.name)
        self.lineEdit_head1.setText('0x'+c_pack.frame_head.hex().upper())
        self.lineEdit_head2.setText('0x'+c_pack.frame_head2.hex().upper())
        self.lineEdit_end1.setText('0x'+c_pack.frame_end.hex().upper())
        self.lineEdit_end2.setText('0x'+c_pack.frame_end2.hex().upper())
        self.lineEdit_pack_info.setText(c_pack.Struct.format)

    def on_lineEdit_end1_editingFinished(self):
        # print('on_lineEdit_end1_editingFinished')
        # text = self.lineEdit_end1.text()
        # if self.pack.str2bytes(str(text)):
        #     pass
        # else:
        #     self.msg_box.my_dialog_msg('输入格式错误')
        #     self.lineEdit_end1.setText('')
        pass

    def on_lineEdit_end2_editingFinished(self):
        # print('on_lineEdit_end2_editingFinished')
        # text = self.lineEdit_end2.text()
        # if self.pack.str2bytes(str(text)):
        #     pass
        # else:
        #     self.msg_box.my_dialog_msg('输入格式错误')
        #     self.lineEdit_end2.setText('')
        pass

    def on_lineEdit_head1_editingFinished(self):
        # print('on_lineEdit_head1_editingFinished')
        text = self.lineEdit_head1.text()
        self.lineEdit_end2.setText(text)

    def on_lineEdit_head2_editingFinished(self):
        text = self.lineEdit_head2.text()
        self.lineEdit_end1.setText(text)

    def check_input_data(self):

        text = self.lineEdit_name.text()
        if text == '':
            name = None
        else:
            name = text
        text = self.lineEdit_head1.text()
        if text == '':
            head1 = None
        else:
            head1 = MyClassPack.str2bytes(str(text))

        text = self.lineEdit_head2.text()
        if text == '':
            head2 = 'no'
        else:
            head2 = MyClassPack.str2bytes(str(text))

        text = self.lineEdit_end1.text()
        if text == '':
            end1 = 'no'
        else:
            end1 = MyClassPack.str2bytes(str(text))

        text = self.lineEdit_end2.text()
        if text == '':
            end2 = None
        else:
            end2 = MyClassPack.str2bytes(str(text))

        text = self.lineEdit_pack_info.text()
        import re
        x = re.findall(r'^[=]{0,1}[<>]{0,1}[iIhHbBcfd]+$', text)
        if len(x):
            fmt = text
        else:
            fmt = None

        msg = ''

        if name is None:
            msg += '名称为空 \n'
        if head1 is None:
            msg += '帖头1err '
        if end1 is None:
            msg += '帖尾1err \n'
        if head2 is None:
            msg += '帖头2err '
        if end2 is None:
            msg += '帖尾2err \n'
        if fmt is None:
            msg += '包信息错误'
        if msg == '':
            if end1 == 'no':
                end1 = b''
            if head2 == 'no':
                head2 = b''
            c_pack = MyClassPack(fmt, head1, head2, end1, end2, name)
            return c_pack
        else:
            self.msg_box.my_dialog_msg(msg)
            return None
            # pass

    def on_pushButton_save_released(self):
        # print('on_pushButton_save_released')
        c_pack = self.check_input_data()
        if c_pack is not None:
            d = c_pack.get_dict()
            self.pack_history[d['name']] = d
            with open('pack_info.json', 'w') as f:
                import json
                json.dump(self.pack_history, f)
                self.msg_box.my_dialog_msg('保存成功')
            self.load_history()

    def on_pushButton_set_pack_released(self):
        # print('on_pushButton_set_pack_released')
        c_pack = self.check_input_data()
        if c_pack is not None:
            self.ser.change_pack(c_pack)
            self.msg_box.my_dialog_msg('设置完成')

    def on_pushButton_set_unpack_released(self):
        # print('on_pushButton_set_unpack_released')
        c_pack = self.check_input_data()
        if c_pack is not None:
            self.ser.change_unpack(c_pack)
            self.msg_box.my_dialog_msg('设置完成')

if __name__ == '__main__':
    plt.ion()
    app = QApplication(sys.argv)
    pyui = PyuiClassFramePackInfo(show=True)
    sys.exit(app.exec())

