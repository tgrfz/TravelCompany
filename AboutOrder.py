import sys
from PyQt5 import QtWidgets, QtCore, Qt
import os
import gui.AboutOrderWindow

class AboutOrderWindow(QtWidgets.QMainWindow, gui.AboutOrderWindow.Ui_AboutOrderWindow):
    def __init__(self, order0):
        super().__init__()
        self.setupUi(self)
        
        self.setWindowIcon(Qt.QIcon(os.path.join(os.path.dirname(__file__), 'resources', 'logo.png')))

        self.order = order0
        self.labelName.setText(self.order.tour.name)
        self.labelCountry.setText(self.order.tour.country)
        self.labelDeparture.setText(self.order.tour.departure)
        self.labelEnd.setText(self.order.tour.end_date.toString(QtCore.Qt.RFC2822Date))
        self.labelStart.setText(self.order.tour.start_date.toString(QtCore.Qt.RFC2822Date))
        self.labelVisa.setText('нужна' if self.order.tour.visa else 'не нужна')
        self.labelPrice.setText('$' + str(self.order.tour.price))

        self.labelFIO.setText(self.order.customer.name)
        self.labelBirth.setText(self.order.customer.date_of_birth.toString(QtCore.Qt.RFC2822Date))
        self.labelPhone.setText(self.order.customer.phone_number)
        self.labelEmail.setText(self.order.customer.email)
        self.labelPassport.setText(self.order.customer.ID)
        self.labelOrderDate.setText(self.order.order_date.toString(QtCore.Qt.RFC2822Date))