import sys
from PyQt5.QtWidgets import QFrame
from PyQt5.QtWidgets import QApplication

from MyClass import MyClassSerial
from PyuiClass.PyuiSetupFrameTest import Ui_Frame
from UiMyBase.UiClassMyBase import UiClassMyBase


class PyuiClassFrameTest(QFrame,Ui_Frame):

    def __init__(self, ser:'MyClassSerial' = None, show = False):
        super(PyuiClassFrameTest, self).__init__()
        self.setupUi(self)
        self.show()

        self.mes_box2 = UiClassMyBase()
        self.mes_box2.my_dialog_yes_no()
        self.mes_box2.trigger.connect(self.test2)

    def test(self, sig):
        print('test', sig)
        pass

    def test2(self, sig):
        print('test2', sig)
        pass

    def on_pushButton_released(self):
        self.mes_box2.my_dialog_yes_no('asdf')

if __name__ == '__main__':
    # plt.ion()
    app = QApplication(sys.argv)
    a = PyuiClassFrameTest()
    sys.exit(app.exec())

