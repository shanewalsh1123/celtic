from datetime import datetime
import os
import pathlib

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

from user_interface import Ui_Form
from utils import annuity_total, interest_only_total, partial_interest_only_total, write_to_file, date_difference


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
        self.ui.interest_type_box.activated[str].connect(self.on_activated)

        self.on_activated(self.ui.interest_type_box.currentText())

    def on_activated(self, text):
        self.combo_text = text
        if self.combo_text == 'PIO':
            self.ui.base_IIOT_input.show()
            self.ui.second_scen_IIOT_input.show()
            self.ui.base_IIOT_label.show()
            self.ui.second_scen_IIOT_label.show()
            self.ui.interest_type_box.setFocus()
        else:
            self.ui.base_IIOT_input.hide()
            self.ui.second_scen_IIOT_input.hide()
            self.ui.base_IIOT_label.hide()
            self.ui.second_scen_IIOT_label.hide()

    def run(self):
        home_dir = pathlib.Path.home()
        desktop = os.path.expanduser('~/Desktop/output.csv')
        filename = qtw.QFileDialog.getSaveFileName(self, 'Save File', desktop)

        n_rows = self.ui.rate_changes_table.rowCount()
        rate_change_list = []
        previous_date = self.ui.date_input.date().toPyDate()
        for i in range(n_rows):
            change_date = self.ui.rate_changes_table.item(i, 0)
            change_rate = self.ui.rate_changes_table.item(i, 1)

            if change_date is not None and change_rate is not None:
                change_date_value = datetime.strptime(change_date.text(), '%d/%m/%Y')
                n_months = date_difference(change_date_value, previous_date)
                change_rate_value = float(change_rate.text())
                if not n_months > 0:
                    qtw.QMessageBox.critical(
                        self, 'Warning', 'Please ensure dates are in the correct order.'
                    )
                    return
                rate_change_list.append([n_months, change_rate_value])
                previous_date = change_date_value

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
