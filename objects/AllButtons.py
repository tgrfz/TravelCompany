from PyQt5 import QtWidgets, QtCore
from objects.AllLists import Lists
from AboutTour import AboutTourWindow
from AboutOrder import AboutOrderWindow
from UpdateTour import UpdateTourWindow

class AllButtonsClass(object):
    def __init__(self):
        self.tour = QtWidgets.QButtonGroup()
        self.atour = QtWidgets.QButtonGroup()
        self.order = QtWidgets.QButtonGroup()
        self.tour.buttonClicked.connect(self.about_tour)
        self.atour.buttonClicked.connect(self.restore_tour)
        self.order.buttonClicked.connect(self.about_order)

    def about_order(self, btn):
        value = Lists.order_list.orders[btn.whatsThis()]
        global win
        win = AboutOrderWindow(value)
        win.show()

    def about_tour(self, btn):
        value = Lists.tour_list.tours[btn.whatsThis()]
        global win
        win = AboutTourWindow(value)
        win.show()

    def restore_tour(self, btn):
        value = Lists.archive_tour_list.tours[btn.whatsThis()]
        global win
        win = UpdateTourWindow(value, flag=False)
        win.show()

class AllButtons():
    buttons = AllButtonsClass()