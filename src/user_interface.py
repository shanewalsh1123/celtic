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
        Form.resize(632, 487)
        self.base_case_label = QtWidgets.QLabel(Form)
        self.base_case_label.setGeometry(QtCore.QRect(40, 20, 211, 31))
        self.base_case_label.setObjectName("base_case_label")
        self.run_button = QtWidgets.QPushButton(Form)
        self.run_button.setGeometry(QtCore.QRect(500, 440, 75, 23))
        self.run_button.setObjectName("run_button")
        self.rate_changes_label = QtWidgets.QLabel(Form)
        self.rate_changes_label.setGeometry(QtCore.QRect(30, 190, 91, 21))
        self.rate_changes_label.setObjectName("rate_changes_label")
        self.drawdown_date_label = QtWidgets.QLabel(Form)
        self.drawdown_date_label.setGeometry(QtCore.QRect(30, 90, 101, 20))
        self.drawdown_date_label.setObjectName("drawdown_date_label")
        self.mortgage_input = QtWidgets.QLineEdit(Form)
        self.mortgage_input.setGeometry(QtCore.QRect(140, 60, 113, 23))
        self.mortgage_input.setObjectName("mortgage_input")
        self.second_scenario_label = QtWidgets.QLabel(Form)
        self.second_scenario_label.setGeometry(QtCore.QRect(390, 170, 181, 31))
        self.second_scenario_label.setObjectName("second_scenario_label")
        self.interest_type_box = QtWidgets.QComboBox(Form)
        self.interest_type_box.setGeometry(QtCore.QRect(140, 150, 111, 22))
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
        self.interest_type_label.setGeometry(QtCore.QRect(40, 150, 81, 21))
        self.interest_type_label.setObjectName("interest_type_label")
        self.mortgage_value_label = QtWidgets.QLabel(Form)
        self.mortgage_value_label.setGeometry(QtCore.QRect(30, 60, 101, 21))
        self.mortgage_value_label.setObjectName("mortgage_value_label")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 220, 241, 251))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.second_scenario_label_2 = QtWidgets.QLabel(Form)
        self.second_scenario_label_2.setGeometry(QtCore.QRect(400, 20, 121, 31))
        self.second_scenario_label_2.setObjectName("second_scenario_label_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(356, 70, 101, 20))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(470, 70, 113, 23))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(350, 100, 91, 31))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(470, 110, 113, 23))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(472, 272, 111, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(356, 230, 101, 20))
        self.label_3.setObjectName("label_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(470, 230, 113, 23))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(350, 260, 91, 31))
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(293, 0, 20, 491))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.base_case_label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Mortgage Description</span></p></body></html>"))
        self.run_button.setText(_translate("Form", "Run"))
        self.rate_changes_label.setText(_translate("Form", "Rate Changes"))
        self.drawdown_date_label.setText(_translate("Form", "Drawdown Date"))
        self.second_scenario_label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Second Scenario</span></p></body></html>"))
        self.interest_type_box.setItemText(0, _translate("Form", "ANN"))
        self.interest_type_box.setItemText(1, _translate("Form", "IOM"))
        self.interest_type_box.setItemText(2, _translate("Form", "PIO"))
        self.interest_rate_label.setText(_translate("Form", "Initial Interest Rate"))
        self.interest_type_label.setText(_translate("Form", "Interest Type"))
        self.mortgage_value_label.setText(_translate("Form", "Mortgage Value"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Form", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Form", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Form", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Form", "5"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("Form", "6"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("Form", "7"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("Form", "8"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("Form", "9"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("Form", "10"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Date"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Interest Rate"))
        self.second_scenario_label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Base Case</span></p></body></html>"))
        self.label.setText(_translate("Form", "Full Term"))
        self.label_2.setText(_translate("Form", "Initial Interest\n"
" Only Term"))
        self.label_3.setText(_translate("Form", "Full Term"))
        self.label_4.setText(_translate("Form", "Initial Interest\n"
" Only Term"))

