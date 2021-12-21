# Basket can have only 8 piece: 0=cpu; 1=mobo; 2=ram; 3=gpu; 4=cooler; 5=psu; 6=case; 7=memory;
import string
from array import array


class Trolley():
    def __init__(self):
        self.trolley = [None] * 7

    def Insert(self, id, i):
        self.trolley[i] = id

    def Remove(self, i):
        self.trolley[i] = None

    def returnList(self):
        return self.trolley
