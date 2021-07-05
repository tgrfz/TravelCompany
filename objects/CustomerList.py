from objects.AbstractList import AbstractList
from objects.Customer import Customer
from PyQt5 import QtWidgets
from PyQt5 import Qt
from PyQt5 import QtCore

class CustomerList(AbstractList):
    def __init__(self):
        self.customers = {}
        self.chosen = Customer()

    def append(self, value):
        if isinstance(value, Customer):
            if value.isValid():
                self.customers[value.ID] = value
            else:
                raise ValueError("Invalid data") 
        else:
            raise TypeError("The object's type is not Customer")

    def to_dict(self):
        fields = []
        for i in self.customers:
            fields.append(self.customers[i].to_dict())
        return fields

    def from_dict(self, fields):
        self.customers = {}
        for i in fields:
            c = Customer().from_dict(i)
            self.customers[c.ID] = c
        return self