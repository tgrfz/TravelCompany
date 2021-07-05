import sys
from PyQt5 import QtWidgets, Qt, QtCore
import os
import gui.NewOrderWindow
from objects.Order import Order
from objects.Tour import Tour
from objects.Customer import Customer
from objects.AllLists import Lists
from ChooseCustomer import ChooseCustomerWindow

class NewOrderWindow(QtWidgets.QMainWindow, gui.NewOrderWindow.Ui_NewOrderWindow):
    def __init__(self, tour0):
        super().__init__()
        self.setupUi(self)

        self.setWindowIcon(Qt.QIcon(os.path.join(os.path.dirname(__file__), 'resources', 'logo.png')))
        self.tour = tour0

        self.labelName.setText(self.tour.name)
        self.labelCountry.setText(self.tour.country)
        self.labelDeparture.setText(self.tour.departure)
        self.labelEnd.setText(self.tour.end_date.toString())
        self.labelStart.setText(self.tour.start_date.toString())
        self.labelVisa.setText('нужна' if self.tour.visa else 'не нужна')
        self.labelPrice.setText('$' + str(self.tour.price))
        self.dateBirth.setMaximumDate(QtCore.QDate.currentDate())

        self.buttonMakeOrder.clicked.connect(self.make_order)
        self.buttonChoose.clicked.connect(self.choose_customer)

    def make_order(self):
        order = Order()
        temp = QtCore.QDateTime.currentDateTime()
        order.ID = ''.join([temp.toString(QtCore.Qt.ISODate),":",str(temp.time().msec())])
        order.tour = self.tour
        order.order_date = QtCore.QDateTime.currentDateTime()
        order.customer = Customer()
        order.customer.name = self.lineName.text()
        order.customer.date_of_birth = self.dateBirth.date()
        order.customer.phone_number = self.linePhone.text()
        order.customer.email = self.lineEmail.text()
        order.customer.ID = self.linePassport.text()
        try:
            Lists.add_order(order)
            Lists.add_customer(order.customer)
            self.close()
        except Exception as e:
            global mb
            mb = QtWidgets.QMessageBox()
            mb.setWindowTitle("error")
            mb.setText(str(e))
            mb.setDefaultButton(QtWidgets.QPushButton("Ок"))
            mb.setWindowIcon(Qt.QIcon(os.path.join(os.path.dirname(__file__), 'resources', 'logo.png')))
            mb.show()
            

    def choose_customer(self):
        global choose_customer_window
        choose_customer_window = ChooseCustomerWindow()
        choose_customer_window.setWindowModality(QtCore.Qt.ApplicationModal)
        choose_customer_window.show()
        choose_customer_window.chosen_signal.connect(self.fill_customer)

    def fill_customer(self):
        cst = Lists.customer_list.chosen
        self.lineName.setText(cst.name)
        self.dateBirth.setDate(cst.date_of_birth)
        self.linePhone.setText(cst.phone_number)
        self.lineEmail.setText(cst.email)
        self.linePassport.setText(cst.ID)