from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

from user_interface import Ui_Form


class UserInterface(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)


if __name__ == '__main__':
     app = qtw.QApplication([])

     widget = UserInterface()
     widget.show()

     app.exec_()
