# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Projects\travelcompany\gui\ChooseCustomerWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ChooseCustomerWindow(object):
    def setupUi(self, ChooseCustomerWindow):
        ChooseCustomerWindow.setObjectName("ChooseCustomerWindow")
        ChooseCustomerWindow.resize(454, 444)
        ChooseCustomerWindow.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(248, 248, 248)")
        self.centralwidget = QtWidgets.QWidget(ChooseCustomerWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listCustomers = QtWidgets.QListWidget(self.centralwidget)
        self.listCustomers.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255)")
        self.listCustomers.setObjectName("listCustomers")
        self.verticalLayout.addWidget(self.listCustomers)
        self.buttonChoose = QtWidgets.QPushButton(self.centralwidget)
        self.buttonChoose.setStyleSheet("background-color: rgb(246, 246, 246);")
        self.buttonChoose.setObjectName("buttonChoose")
        self.verticalLayout.addWidget(self.buttonChoose)
        ChooseCustomerWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ChooseCustomerWindow)
        QtCore.QMetaObject.connectSlotsByName(ChooseCustomerWindow)

    def retranslateUi(self, ChooseCustomerWindow):
        _translate = QtCore.QCoreApplication.translate
        ChooseCustomerWindow.setWindowTitle(_translate("ChooseCustomerWindow", "MainWindow"))
        self.buttonChoose.setText(_translate("ChooseCustomerWindow", "Выбрать"))

