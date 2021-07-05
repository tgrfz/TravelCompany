# from objects.OrderList import OrderList
from PyQt5 import QtCore

class Customer(object):
    def __init__(self):
        self.name = ""
        self.date_of_birth = QtCore.QDate(1,1,1)
        self.phone_number = ""
        self.email = ""
        self.ID = ""
        #self.orders = OrderList()

    def to_dict(self):
        fields = {
            'name': self.name,
            'date_of_birth': self.date_of_birth.toString(),
            'phone_number': self.phone_number,
            'email': self.email,
            'passport_ID': self.ID,
        }
        return fields

    def from_dict(self, fields):
        self.name = fields['name']
        self.date_of_birth = QtCore.QDate.fromString(fields['date_of_birth'])
        self.phone_number = fields['phone_number']
        self.email = fields['email']
        self.ID = fields['passport_ID']
        return self

    def isValid(self):
        if self.name == "" or self.phone_number == "" or self.email == "" or self.ID == "":
            return False
        return True