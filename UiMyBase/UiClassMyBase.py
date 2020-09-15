# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QDialog
from UiMyBase.UiSetUpDialogMsg import Ui_DialogMsg
from UiMyBase.UiSetUpDialogYesNo import Ui_DialogYesNo
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QThread, pyqtSignal


class UiClassMyBase(QThread):
    trigger = pyqtSignal(bool)
    def __init__(self):
        super().__init__()

        self.dialog_msg = QDialog(flags=QtCore.Qt.Dialog)
        self.ui_dialog_msg = Ui_DialogMsg()
        self.ui_dialog_msg.setupUi(self.dialog_msg)

        self.dialog_msg.setFixedSize(self.dialog_msg.width(), self.dialog_msg.height())
        self.dialog_msg.setWindowFlag(Qt.WindowCloseButtonHint)

        self.dialog_yes_no = QDialog(flags=QtCore.Qt.Dialog)
        self.ui_dialog_yn = Ui_DialogYesNo()
        self.ui_dialog_yn.setupUi(self.dialog_yes_no)

        self.ui_dialog_yn.buttonBox.accepted.connect(self.yes_no_accept)
        self.ui_dialog_yn.buttonBox.rejected.connect(self.yes_no_reject)

        self.dialog_yes_no.setFixedSize(self.dialog_yes_no.width(), self.dialog_yes_no.height())
        self.dialog_yes_no.setWindowFlag(Qt.WindowCloseButtonHint)

        # self.my_dialog_yes_no()

    def my_layout(self, parent=None, x=0, y=0, xx=1, yy=1):
        if parent is not None:
            try:
                parent.gridLayout.addWidget(self, x, y, xx, yy)
            except AttributeError:
                print("no gridayou")

    def my_dialog_yes_no(self, msg:'str'='确定?'):
        self.ui_dialog_yn.label_msg.setText(msg)
        self.dialog_yes_no.show()

    def my_dialog_msg(self, msg:'str'='提示'):
        self.ui_dialog_msg.label_msg.setText(msg)
        # if self.dialog_msg is not None:
        #     self.dialog_msg.close()
        self.dialog_msg.show()

    def yes_no_accept(self):
        # print('accept')
        self.trigger.emit(True)

    def yes_no_reject(self):
        # print('reject')
        self.trigger.emit(False)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    x = UiClassMyBase()
    sys.exit(app.exec())
