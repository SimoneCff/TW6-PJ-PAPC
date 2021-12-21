# Basket can have only 8 piece: 0=cpu; 1=mobo; 2=ram; 3=gpu; 4=cooler; 5=psu; 6=case; 7=memory;

from db import searchviaid
from bson.json_util import dumps


class Trolley():
    def __init__(self):
        self.trolley = [None] * 7
        self.totalwatt = 0

    def Insert(self, id, i, dat):
        Query = searchviaid(id, dat).findquery()
        self.trolley[i] = (dumps(Query['name']), dumps(Query['COSTO']), dumps(Query['Watt']), i)
        if i != 5:
            watt = dumps(Query['Watt'])
            watt = watt.split('"', 1)[1]
            watt = watt.split('"', 1)[0]
            self.totalwatt += int(watt)

    def Remove(self, i):
        rem = self.trolley[i]
        self.totalwatt -= rem[3]
        self.trolley[i] = None

    def returnList(self):
        return self.trolley

    def SeeWatt(self):
        return self.totalwatt

