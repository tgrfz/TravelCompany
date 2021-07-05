from PyQt5 import QtCore

class Tour(object):
    def __new__(cls):
        return super(Tour, cls).__new__(cls)

    def __init__(self):
        self.ID = ""
        self.name = ""
        self.price = 0.0
        self.country = ""
        self.start_date = QtCore.QDate(1,1,1)
        self.end_date = QtCore.QDate(1,1,1)
        self.visa = False
        self.description = ""
        self.departure = ""
        # self.status = True

    def isValid(self):
        if self.name == "" or self.country == "" or self.departure == "":
            return False
        if self.start_date > self.end_date:
            return False
        if self.end_date <= QtCore.QDate.currentDate():
            return False
        return True

    def to_dict(self):
        fields = {
            'ID': self.ID,
            'name': self.name,
            'price': self.price,
            'country': self.country,
            'start_date': self.start_date.toString(),
            'end_date': self.end_date.toString(),
            'visa': self.visa,
            'description': self.description,
            'departure': self.departure,
            # self.status
        }
        return fields

    def from_dict(self, fields):
        self.ID = fields['ID']
        self.name = fields['name']
        self.price = fields['price']
        self.country = fields['country']
        self.start_date = QtCore.QDate.fromString(fields['start_date'])
        self.end_date = QtCore.QDate.fromString(fields['end_date'])
        self.visa = fields['visa']
        self.description = fields['description']
        self.departure = fields['departure']
        return self
