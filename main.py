import sys
from PyQt5 import QtWidgets, Qt, QtCore, QtGui
import os
import gui.MainWindow
import gui.AuthorizationWindow
from AddTour import AddTourWindow
from objects.AllLists import Lists
from objects.TourBlock import TourBlock
from objects.OrderBlock import OrderBlock
from objects.ArchiveTourBlock import ArchiveTourBlock
from objects.CustomerBlock import CustomerBlock
import pymongo

class AuthorizationWindow(QtWidgets.QMainWindow, gui.AuthorizationWindow.Ui_AuthorizationWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(Qt.QIcon(os.path.join(os.path.dirname(__file__), 'resources', 'logo.png')))

        client = pymongo.MongoClient()
        db = client['travelcompany']
        self.coll = db['passwords']

        self.buttonLogIn.clicked.connect(self.check_password)

    def check_password(self):
        lg = self.lineLogin.text()
        ps = self.linePassword.text()
        for i in self.coll.find({'login': lg, 'password': ps}):
            global window
            window = MainWindow()
            window.show()
            self.close()
            return
        global mb
        mb = QtWidgets.QMessageBox()
        mb.setText("Неправильный логин или пароль")
        mb.setDefaultButton(QtWidgets.QPushButton("Закрыть"))
        mb.setWindowIcon(Qt.QIcon(os.path.join(os.path.dirname(__file__), 'resources', 'logo.png')))
        mb.show()

class MainWindow(QtWidgets.QMainWindow, gui.MainWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        Lists.load()
        self.update_tours()

        self.set_buttons()
        self.set_icons()

    def set_buttons(self):
        self.buttonTours.clicked.connect(self.change_page_tours)
        self.buttonOrders.clicked.connect(self.change_page_orders)
        self.buttonCustomers.clicked.connect(self.change_page_customers)
        self.buttonToursArchive.clicked.connect(self.change_page_tours_archive)
        self.buttonAbout.clicked.connect(self.change_page_about)
        self.buttonAddTour.clicked.connect(self.add_tour)

    def change_page_tours(self):
        self.stackedWidget.setCurrentIndex(0)
        self.update_tours()
    def change_page_orders(self):
        self.stackedWidget.setCurrentIndex(1)
        self.update_orders()
    def change_page_customers(self):
        self.stackedWidget.setCurrentIndex(2)
        self.update_customers()
    def change_page_tours_archive(self):
        self.stackedWidget.setCurrentIndex(3)
        self.update_tours_archive()
    def change_page_about(self):
        self.stackedWidget.setCurrentIndex(4)

    def set_icons(self):
        self.buttonTours.setIcon(Qt.QIcon(os.path.join(os.path.dirname(__file__), 'resources', 'tour.png')))
        self.buttonOrders.setIcon(Qt.QIcon(os.path.join(os.path.dirname(__file__), 'resources', 'checklist.png')))
        self.buttonCustomers.setIcon(Qt.QIcon(os.path.join(os.path.dirname(__file__), 'resources', 'user.png')))
        self.buttonToursArchive.setIcon(Qt.QIcon(os.path.join(os.path.dirname(__file__), 'resources', 'tour_archive.png')))
        self.buttonAbout.setIcon(Qt.QIcon(os.path.join(os.path.dirname(__file__), 'resources', 'info.png')))
        self.buttonAddTour.setIcon(Qt.QIcon(os.path.join(os.path.dirname(__file__), 'resources', 'plus.png')))
        self.labelLogo.setPixmap(QtGui.QPixmap(os.path.join(os.path.dirname(__file__), 'resources', 'logo.png')))
        self.setWindowIcon(Qt.QIcon(os.path.join(os.path.dirname(__file__), 'resources', 'logo.png')))

    def add_tour(self):
        global add_tour_window
        add_tour_window = AddTourWindow()
        add_tour_window.setWindowModality(QtCore.Qt.ApplicationModal)
        add_tour_window.show()
        add_tour_window.add_tour_signal.connect(self.update_tours)

    def update_tours(self):
        for i in range(self.scrollTourListContents.layout().count()):
            self.scrollTourListContents.layout().itemAt(0).widget().setParent(None)
        for tour in Lists.tour_list.tours:
            self.scrollTourListContents.layout().addWidget(TourBlock(Lists.tour_list.tours[tour]))
        block = QtWidgets.QLabel()
        block.setSizePolicy(Qt.QSizePolicy.Expanding, Qt.QSizePolicy.Expanding)
        self.scrollTourListContents.layout().addWidget(block)

    def update_orders(self):
        for i in range(self.scrollOrderListContents.layout().count()):
            self.scrollOrderListContents.layout().itemAt(0).widget().setParent(None)
        for order in Lists.order_list.orders:
            self.scrollOrderListContents.layout().addWidget(OrderBlock(Lists.order_list.orders[order]))
        block = QtWidgets.QLabel()
        block.setSizePolicy(Qt.QSizePolicy.Expanding, Qt.QSizePolicy.Expanding)
        self.scrollOrderListContents.layout().addWidget(block)

    def update_tours_archive(self):
        for i in range(self.scrollArchiveTourListContents.layout().count()):
            self.scrollArchiveTourListContents.layout().itemAt(0).widget().setParent(None)
        for tour in Lists.archive_tour_list.tours:
            self.scrollArchiveTourListContents.layout().addWidget(ArchiveTourBlock(Lists.archive_tour_list.tours[tour]))
        block = QtWidgets.QLabel()
        block.setSizePolicy(Qt.QSizePolicy.Expanding, Qt.QSizePolicy.Expanding)
        self.scrollArchiveTourListContents.layout().addWidget(block)

    def update_customers(self):
        for i in range(self.scrollCustomerListContents.layout().count()):
            self.scrollCustomerListContents.layout().itemAt(0).widget().setParent(None)
        for customer in Lists.customer_list.customers:
            self.scrollCustomerListContents.layout().addWidget(CustomerBlock(Lists.customer_list.customers[customer]))
        block = QtWidgets.QLabel()
        block.setSizePolicy(Qt.QSizePolicy.Expanding, Qt.QSizePolicy.Expanding)
        self.scrollCustomerListContents.layout().addWidget(block)

def main():
    app = QtWidgets.QApplication(sys.argv)
    awindow = AuthorizationWindow()
    awindow.show()  
    # window = MainWindow()
    # window.show()
    app.exec_()

if __name__ == '__main__':
    main()