from objects.AbstractList import AbstractList
from objects.Order import Order

class OrderList(AbstractList):
    def __init__(self):
        self.orders = {}

    def append(self, value):
        if isinstance(value, Order):
            if value.isValid():
                self.orders[value.ID] = value
            else:
                raise ValueError("Invalid data") 
        else:
            raise TypeError("The object's type is not Tour")

    def to_dict(self):
        fields = []
        for i in self.orders:
            fields.append(self.orders[i].to_dict())
        return fields

    def from_dict(self, fields):
        self.orders = {}
        for i in fields:
            o = Order().from_dict(i)
            self.orders[o.ID] = o
        return self