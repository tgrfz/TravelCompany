import sys
from PyQt5 import QtWidgets, QtCore, Qt
import os
import gui.UpdateTourWindow
from objects.Tour import Tour
from objects.AllLists import Lists

class UpdateTourWindow(QtWidgets.QMainWindow, gui.UpdateTourWindow.Ui_UpdateTourWindow):
    def __init__(self, tour, flag = True): # flag == True - update tour; flag == False - restore archive tour
        super().__init__()
        self.setupUi(self)

        self.setWindowIcon(Qt.QIcon(os.path.join(os.path.dirname(__file__), 'resources', 'logo.png')))
        if flag:
            self.setWindowTitle("Изменение тура")
        else:
            self.setWindowTitle("Восстановление тура")

        self.labelName.setText(tour.name)
        self.labelCountry.setText(tour.country)
        self.labelDeparture.setText(tour.departure)
        self.dateEnd.setDate(tour.end_date)
        self.dateStart.setDate(tour.start_date)
        self.checkBoxVisa.setChecked(tour.visa)
        self.textDescription.setPlainText(tour.description)
        self.doubleSpinPrice.setValue(tour.price)

        self.tour = tour
        self.flag = flag
        self.buttonSave.clicked.connect(self.save)

    def save(self):
        self.tour.start_date = self.dateStart.date()
        self.tour.end_date = self.dateEnd.date()
        self.tour.price = self.doubleSpinPrice.value()
        self.tour.visa = self.checkBoxVisa.isChecked()
        self.tour.description = self.textDescription.toPlainText()
        try:
            if self.flag:
                Lists.update_tour(self.tour)
                self.close()
            else:
                Lists.add_tour(self.tour)
                Lists.delete_archive_tour(self.tour)
                self.close()
        except Exception as e:
            global mb
            mb = QtWidgets.QMessageBox()
            mb.setWindowTitle("error")
            mb.setText(str(e))
            mb.setDefaultButton(QtWidgets.QPushButton("Ok"))
            mb.setWindowIcon(Qt.QIcon(os.path.join(os.path.dirname(__file__), 'resources', 'logo.png')))
            mb.show()