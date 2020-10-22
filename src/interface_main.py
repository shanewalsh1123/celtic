from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

from user_interface import Ui_Form
from utils import annuity_total


class UserInterface(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Validators
        self.onlyInt = qtg.QIntValidator()
        self.onlyFloat = qtg.QDoubleValidator()
        self.ui.mortgage_input.setValidator(self.onlyInt)
        self.ui.initial_interest_input.setValidator(self.onlyFloat)
        self.ui.base_full_term_input.setValidator(self.onlyInt)

        # Connections
        self.ui.run_button.clicked.connect(self.run)

    def run(self):
        try:
            mortgage_value = int(self.ui.mortgage_input.text())
            interest_rate = float(self.ui.initial_interest_input.text()) / (100 * 12)
            term_length = int(self.ui.base_full_term_input.text())
        except ValueError:
            qtw.QMessageBox.critical(
                self, 'Warning', 'Please ensure all information is put in correctly'
            )
            return

        interest_paid = annuity_total(mortgage_value, interest_rate, term_length) - mortgage_value


if __name__ == '__main__':
    app = qtw.QApplication([])

    widget = UserInterface()
    widget.show()

    app.exec_()
