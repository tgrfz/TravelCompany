# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Projects\travelcompany\gui\AboutTourWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AboutTourWindow(object):
    def setupUi(self, AboutTourWindow):
        AboutTourWindow.setObjectName("AboutTourWindow")
        AboutTourWindow.resize(621, 685)
        AboutTourWindow.setAutoFillBackground(False)
        AboutTourWindow.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(248, 248, 248)")
        self.centralwidget = QtWidgets.QWidget(AboutTourWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelName = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelName.sizePolicy().hasHeightForWidth())
        self.labelName.setSizePolicy(sizePolicy)
        self.labelName.setStyleSheet("font: 13pt \"MS Shell Dlg 2\";")
        self.labelName.setAlignment(QtCore.Qt.AlignCenter)
        self.labelName.setObjectName("labelName")
        self.verticalLayout.addWidget(self.labelName)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout_2.setContentsMargins(11, 11, 11, 11)
        self.formLayout_2.setHorizontalSpacing(10)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.labelCountry = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelCountry.sizePolicy().hasHeightForWidth())
        self.labelCountry.setSizePolicy(sizePolicy)
        self.labelCountry.setText("")
        self.labelCountry.setObjectName("labelCountry")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.labelCountry)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.labelPrice = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelPrice.sizePolicy().hasHeightForWidth())
        self.labelPrice.setSizePolicy(sizePolicy)
        self.labelPrice.setText("")
        self.labelPrice.setObjectName("labelPrice")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.labelPrice)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.labelDeparture = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelDeparture.sizePolicy().hasHeightForWidth())
        self.labelDeparture.setSizePolicy(sizePolicy)
        self.labelDeparture.setText("")
        self.labelDeparture.setObjectName("labelDeparture")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.labelDeparture)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.labelStart = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelStart.sizePolicy().hasHeightForWidth())
        self.labelStart.setSizePolicy(sizePolicy)
        self.labelStart.setText("")
        self.labelStart.setObjectName("labelStart")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.labelStart)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.labelEnd = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelEnd.sizePolicy().hasHeightForWidth())
        self.labelEnd.setSizePolicy(sizePolicy)
        self.labelEnd.setText("")
        self.labelEnd.setObjectName("labelEnd")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.labelEnd)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.labelVisa = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelVisa.sizePolicy().hasHeightForWidth())
        self.labelVisa.setSizePolicy(sizePolicy)
        self.labelVisa.setText("")
        self.labelVisa.setObjectName("labelVisa")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.labelVisa)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(7, 7, 7, 7)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textDescription = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textDescription.sizePolicy().hasHeightForWidth())
        self.textDescription.setSizePolicy(sizePolicy)
        self.textDescription.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.textDescription.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textDescription.setLineWidth(0)
        self.textDescription.setObjectName("textDescription")
        self.verticalLayout_2.addWidget(self.textDescription)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonToArchive = QtWidgets.QPushButton(self.centralwidget)
        self.buttonToArchive.setEnabled(True)
        self.buttonToArchive.setMinimumSize(QtCore.QSize(0, 35))
        self.buttonToArchive.setStyleSheet("background-color: rgb(246, 246, 246);")
        self.buttonToArchive.setObjectName("buttonToArchive")
        self.horizontalLayout.addWidget(self.buttonToArchive)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.buttonUpdate = QtWidgets.QPushButton(self.centralwidget)
        self.buttonUpdate.setObjectName("buttonUpdate")
        self.horizontalLayout.addWidget(self.buttonUpdate)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.buttonMakeOrder = QtWidgets.QPushButton(self.centralwidget)
        self.buttonMakeOrder.setMinimumSize(QtCore.QSize(0, 35))
        self.buttonMakeOrder.setStyleSheet("background-color: rgb(246, 246, 246);")
        self.buttonMakeOrder.setObjectName("buttonMakeOrder")
        self.horizontalLayout.addWidget(self.buttonMakeOrder)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 2)
        self.horizontalLayout.setStretch(3, 1)
        self.horizontalLayout.setStretch(4, 2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        AboutTourWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AboutTourWindow)
        QtCore.QMetaObject.connectSlotsByName(AboutTourWindow)

    def retranslateUi(self, AboutTourWindow):
        _translate = QtCore.QCoreApplication.translate
        AboutTourWindow.setWindowTitle(_translate("AboutTourWindow", "Информация о туре"))
        self.labelName.setText(_translate("AboutTourWindow", "Название тура"))
        self.label_6.setText(_translate("AboutTourWindow", "Страна:"))
        self.label_7.setText(_translate("AboutTourWindow", "Цена:"))
        self.label_8.setText(_translate("AboutTourWindow", "Место отправления:"))
        self.label_9.setText(_translate("AboutTourWindow", "Дата выезда:"))
        self.label_10.setText(_translate("AboutTourWindow", "Дата приезда:"))
        self.label_11.setText(_translate("AboutTourWindow", "Виза:"))
        self.textDescription.setHtml(_translate("AboutTourWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.buttonToArchive.setText(_translate("AboutTourWindow", "Архивировать"))
        self.buttonUpdate.setText(_translate("AboutTourWindow", "Редактировать"))
        self.buttonMakeOrder.setText(_translate("AboutTourWindow", "Оформить заказ"))

