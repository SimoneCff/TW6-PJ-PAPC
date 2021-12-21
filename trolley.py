# Basket can have only 8 piece: 0=cpu; 1=mobo; 2=ram; 3=gpu; 4=cooler; 5=psu; 6=case; 7=memory;

from db import searchviaid
from bson.json_util import dumps


class Trolley():
    def __init__(self):
        self.TotalWatt = None
        self.trolley = [None] * 7

    def Insert(self, id, i, dat):
        print(id, i, dat)
        Query = searchviaid(id, dat).findquery()
        self.trolley[i] = (dumps(Query['name']), dumps(Query['COSTO']), dumps(Query['Watt']))

    def Remove(self, i):
        self.trolley[i] = None

    def returnList(self):
        return self.trolley
