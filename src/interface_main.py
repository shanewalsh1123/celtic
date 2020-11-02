import os
import pathlib

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

from user_interface import Ui_Form
from utils import annuity_total, interest_only_total, partial_interest_only_total, write_to_file


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
        self.ui.second_scen_full_term_input.setValidator(self.onlyInt)
        self.ui.base_IIOT_input.setValidator(self.onlyInt)
        self.ui.second_scen_IIOT_input.setValidator(self.onlyInt)

        # Connections
        self.ui.run_button.clicked.connect(self.run)

    def run(self):
        home_dir = pathlib.Path.home()
        desktop = os.path.expanduser('~/Desktop/output.csv')
        filename = qtw.QFileDialog.getSaveFileName(self, 'Save File', desktop)

        if not filename[0]:
            return

        try:
            mortgage_value = int(self.ui.mortgage_input.text())
            interest_rate = float(self.ui.initial_interest_input.text()) / (100 * 12)
            term_length_base = int(self.ui.base_full_term_input.text())
            term_length_second = int(self.ui.second_scen_full_term_input.text())
            if self.ui.interest_type_box.currentText() == 'PIO':
                IO_term_length_base = int(self.ui.base_IIOT_input.text())
                IO_term_length_second = int(self.ui.second_scen_IIOT_input.text())

        except ValueError:
            qtw.QMessageBox.critical(
                self, 'Warning', 'Please ensure all information is put in correctly'
            )
            return

        if self.ui.interest_type_box.currentText() == 'ANN':
            interest_paid_base = annuity_total(mortgage_value, interest_rate, term_length_base) - mortgage_value
            interest_paid_second = annuity_total(mortgage_value, interest_rate, term_length_second) - mortgage_value
        elif self.ui.interest_type_box.currentText() == 'IOM':
            interest_paid_base = interest_only_total(mortgage_value, interest_rate, term_length_base) - mortgage_value
            interest_paid_second = interest_only_total(mortgage_value, interest_rate, term_length_second) - mortgage_value
        elif self.ui.interest_type_box.currentText() == 'PIO':
            interest_paid_base = partial_interest_only_total(mortgage_value, interest_rate, term_length_base, IO_term_length_base) - mortgage_value
            interest_paid_second = partial_interest_only_total(mortgage_value, interest_rate, term_length_second, IO_term_length_second) - mortgage_value
        base_minus_second = interest_paid_base - interest_paid_second
        labels = [
            'Mortgage Value',
            'Initial Interest Rate',
            'Base Term Length',
            'Second Scenario Term Length',
            'Interest Paid Base',
            'Interest Paid Second',
            'Difference'
        ]
        data = [
            mortgage_value,
            interest_rate,
            term_length_base,
            term_length_second,
            interest_paid_base,
            interest_paid_second,
            base_minus_second,
        ]
        write_to_file(filename[0], labels, data)


if __name__ == '__main__':
    app = qtw.QApplication([])

    widget = UserInterface()
    widget.show()

    app.exec_()
