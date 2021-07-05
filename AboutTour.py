import sys
from PyQt5 import QtWidgets, QtCore, Qt
import os
import gui.AboutTourWindow
from NewOrder import NewOrderWindow
from UpdateTour import UpdateTourWindow
from objects.AllLists import Lists

class AboutTourWindow(QtWidgets.QMainWindow, gui.AboutTourWindow.Ui_AboutTourWindow):
    def __init__(self, tour0):
        super().__init__()
        self.setupUi(self)

        self.setWindowIcon(Qt.QIcon(os.path.join(os.path.dirname(__file__), 'resources', 'logo.png')))
        self.tour = tour0

        self.labelName.setText(self.tour.name)
        self.labelCountry.setText(self.tour.country)
        self.labelDeparture.setText(self.tour.departure)
        self.labelEnd.setText(self.tour.end_date.toString(QtCore.Qt.RFC2822Date))
        self.labelStart.setText(self.tour.start_date.toString(QtCore.Qt.RFC2822Date))
        self.labelVisa.setText('нужна' if self.tour.visa else 'не нужна')
        self.textDescription.setText(self.tour.description)
        self.labelPrice.setText('$' + str(self.tour.price))

        self.buttonMakeOrder.clicked.connect(self.make_order)
        self.buttonUpdate.clicked.connect(self.update)
        self.buttonToArchive.clicked.connect(self.to_archive)

    def make_order(self):
        global new_order_window
        new_order_window = NewOrderWindow(self.tour)
        new_order_window.setWindowModality(QtCore.Qt.ApplicationModal)
        new_order_window.show()
        self.close()

    def update(self):
        global new_update_window
        new_update_window = UpdateTourWindow(self.tour)
        new_update_window.setWindowModality(QtCore.Qt.ApplicationModal)
        new_update_window.show()
        self.close()

    def to_archive(self):
        Lists.delete_tour(self.tour)
        Lists.add_archive_tour(self.tour)
        global mb
        mb = QtWidgets.QMessageBox()
        mb.setWindowTitle("")
        mb.setText("Тур архивирован")
        mb.setDefaultButton(QtWidgets.QPushButton("Ok"))
        mb.setWindowIcon(Qt.QIcon(os.path.join(os.path.dirname(__file__), 'resources', 'logo.png')))
        mb.show()
        self.close()