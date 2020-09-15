# -*- coding: UTF-8 -*-

import sys
from PyQt5.QtWidgets import QApplication

class PyuiClassMyBase(object):

    def __init__(self):
        pass

    def my_layout(self, parent=None, x=0, y=0, xx=1, yy=1):
        if parent is not None:
            try:
                parent.gridLayout.addWidget(self, x, y, xx, yy)
            except AttributeError:
                print("no gridayou")

    @staticmethod
    def bit_to_str_show(bit:'bytes'):
        print(bit.split(), end='')





