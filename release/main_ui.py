# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form_1(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1126, 724)
        self.name_input = QtWidgets.QLineEdit(parent=Form)
        self.name_input.setGeometry(QtCore.QRect(90, 30, 131, 20))
        self.name_input.setObjectName("name_input")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(30, 30, 51, 20))
        self.label.setObjectName("label")
        self.choose_st_ob = QtWidgets.QComboBox(parent=Form)
        self.choose_st_ob.setGeometry(QtCore.QRect(360, 30, 141, 22))
        self.choose_st_ob.setObjectName("choose_st_ob")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(250, 30, 101, 20))
        self.label_2.setObjectName("label_2")
        self.choose_type = QtWidgets.QComboBox(parent=Form)
        self.choose_type.setGeometry(QtCore.QRect(540, 30, 151, 22))
        self.choose_type.setObjectName("choose_type")
        self.tableWidget = QtWidgets.QTableWidget(parent=Form)
        self.tableWidget.setGeometry(QtCore.QRect(30, 70, 1061, 631))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.search_button = QtWidgets.QPushButton(parent=Form)
        self.search_button.setGeometry(QtCore.QRect(720, 30, 75, 23))
        self.search_button.setObjectName("search_button")
        self.admin_button = QtWidgets.QPushButton(parent=Form)
        self.admin_button.setGeometry(QtCore.QRect(820, 30, 91, 23))
        self.admin_button.setObjectName("admin_button")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Название"))
        self.label_2.setText(_translate("Form", "Степень обжарки"))
        self.search_button.setText(_translate("Form", "Поиск"))
        self.admin_button.setText(_translate("Form", "Изменить БД"))
