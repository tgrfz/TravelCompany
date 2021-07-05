from objects.Tour import Tour
from PyQt5 import QtWidgets, Qt, QtCore
from objects.AllLists import Lists
from objects.AllButtons import AllButtons

class TourBlock(QtWidgets.QFrame):
    def __init__(self, value):
        super().__init__()

        self.setLayout(QtWidgets.QHBoxLayout())
        self.setFrameShape(1)

        frm = QtWidgets.QFrame()
        frm.setLayout(QtWidgets.QVBoxLayout())
        frm.layout().addWidget(QtWidgets.QLabel(value.name))
        frm.layout().addWidget(QtWidgets.QLabel('Страна: {}'.format(value.country)))
        frm.layout().addWidget(QtWidgets.QLabel('Стоимость: ${}'.format(value.price)))
        frm.layout().addWidget(QtWidgets.QLabel('Дата выезда: {}'.format(value.start_date.toString(QtCore.Qt.RFC2822Date))))
        frm.layout().addWidget(QtWidgets.QLabel('Дата приезда: {}'.format(value.end_date.toString(QtCore.Qt.RFC2822Date))))
        frm.layout().itemAt(0).widget().setStyleSheet('font: 13pt "MS Shell Dlg 2";')
        frm.setSizePolicy(Qt.QSizePolicy.Expanding, Qt.QSizePolicy.Minimum)
        self.setStyleSheet('background-color: rgb(252, 252, 252);')
        self.layout().addWidget(frm)

        btn = QtWidgets.QPushButton('Подробнее')
        btn.setWhatsThis(value.ID)
        self.layout().addWidget(btn)
        self.layout().setAlignment(btn, QtCore.Qt.AlignBottom)
        btn.setSizePolicy(Qt.QSizePolicy.Minimum, Qt.QSizePolicy.Minimum)
        btn.setStyleSheet('background-color: rgb(246, 246, 246);')
        AllButtons.buttons.tour.addButton(btn)