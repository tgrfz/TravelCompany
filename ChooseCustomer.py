import sys
from PyQt5 import QtWidgets, QtCore, Qt
import os
import gui.ChooseCustomerWindow
from objects.AllLists import Lists

class ChooseCustomerWindow(QtWidgets.QMainWindow, gui.ChooseCustomerWindow.Ui_ChooseCustomerWindow):
    chosen_signal = QtCore.pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(Qt.QIcon(os.path.join(os.path.dirname(__file__), 'resources', 'logo.png')))

        for i in Lists.customer_list.customers:
            c = Lists.customer_list.customers[i]
            it = QtWidgets.QListWidgetItem(''.join([c.name, ', ', c.ID]))
            self.listCustomers.addItem(it)
    
        self.buttonChoose.clicked.connect(self.choose)
    
    def choose(self):
        txt = self.listCustomers.currentItem().text()
        txt = txt.split(', ')[-1]
        Lists.customer_list.chosen = Lists.customer_list.customers[txt]
        self.chosen_signal.emit()
        self.close()