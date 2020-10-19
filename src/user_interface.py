# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_interface.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(563, 400)
        self.base_case_label = QtWidgets.QLabel(Form)
        self.base_case_label.setGeometry(QtCore.QRect(120, 20, 81, 31))
        self.base_case_label.setObjectName("base_case_label")
        self.run_button = QtWidgets.QPushButton(Form)
        self.run_button.setGeometry(QtCore.QRect(440, 340, 75, 23))
        self.run_button.setObjectName("run_button")
        self.rate_changes_label = QtWidgets.QLabel(Form)
        self.rate_changes_label.setGeometry(QtCore.QRect(40, 150, 91, 21))
        self.rate_changes_label.setObjectName("rate_changes_label")
        self.drawdown_date_label = QtWidgets.QLabel(Form)
        self.drawdown_date_label.setGeometry(QtCore.QRect(30, 90, 101, 20))
        self.drawdown_date_label.setObjectName("drawdown_date_label")
        self.open_rate_changes_button = QtWidgets.QPushButton(Form)
        self.open_rate_changes_button.setGeometry(QtCore.QRect(140, 150, 111, 23))
        self.open_rate_changes_button.setObjectName("open_rate_changes_button")
        self.mortgage_input = QtWidgets.QLineEdit(Form)
        self.mortgage_input.setGeometry(QtCore.QRect(140, 60, 113, 23))
        self.mortgage_input.setObjectName("mortgage_input")
        self.second_scenario_label = QtWidgets.QLabel(Form)
        self.second_scenario_label.setGeometry(QtCore.QRect(376, 20, 111, 31))
        self.second_scenario_label.setObjectName("second_scenario_label")
        self.interest_type_box = QtWidgets.QComboBox(Form)
        self.interest_type_box.setGeometry(QtCore.QRect(140, 180, 111, 22))
        self.interest_type_box.setObjectName("interest_type_box")
        self.interest_type_box.addItem("")
        self.interest_type_box.addItem("")
        self.interest_type_box.addItem("")
        self.initial_interest_input = QtWidgets.QLineEdit(Form)
        self.initial_interest_input.setGeometry(QtCore.QRect(140, 120, 113, 23))
        self.initial_interest_input.setObjectName("initial_interest_input")
        self.date_input = QtWidgets.QDateEdit(Form)
        self.date_input.setGeometry(QtCore.QRect(140, 90, 111, 24))
        self.date_input.setObjectName("date_input")
        self.interest_rate_label = QtWidgets.QLabel(Form)
        self.interest_rate_label.setGeometry(QtCore.QRect(10, 120, 121, 21))
        self.interest_rate_label.setObjectName("interest_rate_label")
        self.interest_type_label = QtWidgets.QLabel(Form)
        self.interest_type_label.setGeometry(QtCore.QRect(40, 180, 81, 21))
        self.interest_type_label.setObjectName("interest_type_label")
        self.mortgage_value_label = QtWidgets.QLabel(Form)
        self.mortgage_value_label.setGeometry(QtCore.QRect(30, 60, 101, 21))
        self.mortgage_value_label.setObjectName("mortgage_value_label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.base_case_label.setText(_translate("Form", "Base Case"))
        self.run_button.setText(_translate("Form", "Run"))
        self.rate_changes_label.setText(_translate("Form", "Rate Changes"))
        self.drawdown_date_label.setText(_translate("Form", "Drawdown Date"))
        self.open_rate_changes_button.setText(_translate("Form", "Browse"))
        self.second_scenario_label.setText(_translate("Form", "Second Scenario"))
        self.interest_type_box.setItemText(0, _translate("Form", "ANN"))
        self.interest_type_box.setItemText(1, _translate("Form", "IOM"))
        self.interest_type_box.setItemText(2, _translate("Form", "PIO"))
        self.interest_rate_label.setText(_translate("Form", "Initial Interest Rate"))
        self.interest_type_label.setText(_translate("Form", "Interest Type"))
        self.mortgage_value_label.setText(_translate("Form", "Mortgage Value"))

