from objects.Tour import Tour
from objects.Customer import Customer
from PyQt5 import QtCore

class Order(object):
    def __init__(self):
        self.ID = 0
        self.tour = Tour()
        self.customer = Customer()
        self.order_date = QtCore.QDate(1,1,1)
        #self.status = ""

    def to_dict(self):
        fields = {
            'ID': self.ID,
            'tour': self.tour.to_dict(),
            'customer': self.customer.to_dict(),
            'order_date': self.order_date.toString(),
        }
        return fields

    def from_dict(self, fields):
        self.ID = fields['ID']
        self.tour = Tour().from_dict(fields['tour'])
        self.customer = Customer().from_dict(fields['customer'])
        self.order_date = QtCore.QDateTime.fromString(fields['order_date'])
        return self

    def isValid(self):
        return (self.tour.isValid() and self.customer.isValid())
