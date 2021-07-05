from objects.Customer import Customer
from PyQt5 import QtWidgets, Qt, QtCore
from objects.AllLists import Lists

class CustomerBlock(QtWidgets.QFrame):
    def __init__(self, value):
        super().__init__()

        self.setLayout(QtWidgets.QHBoxLayout())
        self.setFrameShape(1)

        frm = QtWidgets.QFrame()
        frm.setLayout(QtWidgets.QVBoxLayout())
        frm.layout().addWidget(QtWidgets.QLabel('{}'.format(value.name)))
        frm.layout().addWidget(QtWidgets.QLabel('Дата рождения: {}'.format(value.date_of_birth.toString(QtCore.Qt.RFC2822Date))))
        frm.layout().addWidget(QtWidgets.QLabel('Телефон: {}'.format(value.phone_number)))
        frm.layout().addWidget(QtWidgets.QLabel('Email: {}'.format(value.email)))
        frm.layout().addWidget(QtWidgets.QLabel('Номер паспорта: {}'.format(value.ID)))
        frm.layout().itemAt(0).widget().setStyleSheet('font: 13pt "MS Shell Dlg 2";')
        frm.setSizePolicy(Qt.QSizePolicy.Expanding, Qt.QSizePolicy.Minimum)
        self.setStyleSheet('background-color: rgb(252, 252, 252);')
        self.layout().addWidget(frm)