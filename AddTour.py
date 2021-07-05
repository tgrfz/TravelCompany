import sys
from PyQt5 import QtWidgets, QtCore, Qt
import os
import gui.AddTourWindow
from objects.Tour import Tour
from objects.AllLists import Lists

class AddTourWindow(QtWidgets.QMainWindow, gui.AddTourWindow.Ui_AddTourWindow):
    add_tour_signal = QtCore.pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowIcon(Qt.QIcon(os.path.join(os.path.dirname(__file__), 'resources', 'logo.png')))

        self.buttonAdd.clicked.connect(self.add)

    def add(self):
        tour = Tour()
        temp = QtCore.QDateTime.currentDateTime()
        tour.ID = ''.join([temp.toString(QtCore.Qt.ISODate),":",str(temp.time().msec())])
        tour.name = self.lineName.text()
        tour.country = self.lineCountry.text()
        tour.departure = self.lineDeparture.text()
        tour.start_date = self.dateStart.date()
        tour.end_date = self.dateEnd.date()
        tour.price = self.doubleSpinPrice.value()
        tour.visa = self.checkBoxVisa.isChecked()
        tour.description = self.textDescription.toPlainText()
        try:
            Lists.add_tour(tour)
            self.add_tour_signal.emit()
            self.close()
        except Exception as e:
            global mb
            mb = QtWidgets.QMessageBox()
            mb.setWindowTitle("error")
            mb.setText(str(e))
            mb.setDefaultButton(QtWidgets.QPushButton("Ok"))
            mb.setWindowIcon(Qt.QIcon(os.path.join(os.path.dirname(__file__), 'resources', 'logo.png')))
            mb.show()