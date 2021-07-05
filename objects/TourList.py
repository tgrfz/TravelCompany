from objects.AbstractList import AbstractList
from objects.Tour import Tour

class TourList(AbstractList):
    def __init__(self):
        self.tours = {}

    def append(self, value):
        if isinstance(value, Tour):
            if value.isValid():
                self.tours[value.ID] = value
            else:
                raise ValueError("Invalid data") 
        else:
            raise TypeError("The object's type is not Tour")

    def update(self, value):
        self.append(value)

    def delete(self, value):
        self.tours.pop(value.ID)

    def to_dict(self):
        fields = []
        for i in self.tours:
            fields.append(self.tours[i].to_dict())
        return fields

    def from_dict(self, fields):
        self.tours = {}
        for i in fields:
            t = Tour().from_dict(i)
            self.tours[t.ID] = t
        return self