# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Projects\OOP\travelcompany\gui\AuthorizationWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AuthorizationWindow(object):
    def setupUi(self, AuthorizationWindow):
        AuthorizationWindow.setObjectName("AuthorizationWindow")
        AuthorizationWindow.resize(352, 184)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AuthorizationWindow.sizePolicy().hasHeightForWidth())
        AuthorizationWindow.setSizePolicy(sizePolicy)
        AuthorizationWindow.setStyleSheet("background-color: rgb(248, 248, 248);")
        self.centralwidget = QtWidgets.QWidget(AuthorizationWindow)
        self.centralwidget.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setContentsMargins(25, 25, 25, 25)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineLogin = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineLogin.sizePolicy().hasHeightForWidth())
        self.lineLogin.setSizePolicy(sizePolicy)
        self.lineLogin.setMinimumSize(QtCore.QSize(220, 0))
        self.lineLogin.setObjectName("lineLogin")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineLogin)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.linePassword = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.linePassword.sizePolicy().hasHeightForWidth())
        self.linePassword.setSizePolicy(sizePolicy)
        self.linePassword.setMinimumSize(QtCore.QSize(220, 0))
        self.linePassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.linePassword.setObjectName("linePassword")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.linePassword)
        self.buttonLogIn = QtWidgets.QPushButton(self.centralwidget)
        self.buttonLogIn.setStyleSheet("background-color: rgb(246, 246, 246);")
        self.buttonLogIn.setObjectName("buttonLogIn")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.buttonLogIn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(2, QtWidgets.QFormLayout.SpanningRole, spacerItem)
        AuthorizationWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AuthorizationWindow)
        QtCore.QMetaObject.connectSlotsByName(AuthorizationWindow)

    def retranslateUi(self, AuthorizationWindow):
        _translate = QtCore.QCoreApplication.translate
        AuthorizationWindow.setWindowTitle(_translate("AuthorizationWindow", "Авторизация"))
        self.label.setText(_translate("AuthorizationWindow", "Логин:"))
        self.label_2.setText(_translate("AuthorizationWindow", "Пароль:"))
        self.buttonLogIn.setText(_translate("AuthorizationWindow", "Войти"))

