from objects.Order import Order
from PyQt5 import QtWidgets
from PyQt5 import Qt
from PyQt5 import QtCore
from objects.AllLists import Lists
from objects.AllButtons import AllButtons

class OrderBlock(QtWidgets.QFrame):
    def __init__(self, value):
        super().__init__()

        self.setLayout(QtWidgets.QHBoxLayout())
        self.setFrameShape(1)

        frm = QtWidgets.QFrame()
        frm.setLayout(QtWidgets.QVBoxLayout())
        frm.layout().addWidget(QtWidgets.QLabel('Тур: {}'.format(value.tour.name)))
        frm.layout().addWidget(QtWidgets.QLabel('Заказчик: {}'.format(value.customer.name)))
        frm.setSizePolicy(Qt.QSizePolicy.Expanding, Qt.QSizePolicy.Minimum)
        self.setStyleSheet('background-color: rgb(252, 252, 252);')
        self.layout().addWidget(frm)

        btn = QtWidgets.QPushButton('Подробнее')
        btn.setWhatsThis(value.ID)
        self.layout().addWidget(btn)
        self.layout().setAlignment(btn, QtCore.Qt.AlignBottom)
        btn.setSizePolicy(Qt.QSizePolicy.Minimum, Qt.QSizePolicy.Minimum)
        btn.setStyleSheet('background-color: rgb(246, 246, 246);')
        AllButtons.buttons.order.addButton(btn)