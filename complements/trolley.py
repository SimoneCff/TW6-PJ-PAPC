# Basket can have only 8 piece: 0=cpu; 1=mobo; 2=ram; 3=gpu; 4=cooler; 5=psu; 6=case; 7=memory;

from complements.db import searchviaid
from bson.json_util import dumps


class Trolley():
    def __init__(self):
        self.trolley = [None] * 8
        self.totalwatt = 0

    def Insert(self, id, i, dat):
        Query = searchviaid(id, dat).findquery()
        if i == 6:
            self.trolley[i] = (dumps(Query['name']), dumps(Query['COSTO']), dumps(Query['model']), i)
        else:
            if i == 7:
                self.trolley[i] = (dumps(Query['name']), dumps(Query['COSTO']), None, i)
            else:
                if i == 0:
                    self.trolley[i] = (dumps(Query['name']), dumps(Query['COSTO']), dumps(Query['Watt']),
                                       i, dumps(Query['socket']))
                else:
                    if i == 1:
                        self.trolley[i] = (dumps(Query['name']), dumps(Query['COSTO']), dumps(Query['Watt']), i
                                           ,dumps(Query['socket']), dumps(Query['clock-r']), dumps(Query['model']))
                    else:
                        if i == 2:
                            self.trolley[i] = (dumps(Query['name']), dumps(Query['COSTO']), dumps(Query['clock']), i)
                        else:
                            self.trolley[i] = (dumps(Query['name']), dumps(Query['COSTO']), dumps(Query['Watt']), i)
        if i == 0 or i == 1 or i == 3 or i == 4:
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
        PSU = self.trolley[5]
        if PSU is not None:
            if self.totalwatt < int(PSU[3]):
                return True
            else:
                return False
        else:
            return None

    def SeeCompatibiltyCPU(self):
        CPU = self.trolley[0]
        MOBO = self.trolley[1]
        if CPU is not None and MOBO is not None:
            if CPU[3] == MOBO[3]:
                return True
            else:
                return False
        else :
            return None

    def SeeCompatibiltyRAM(self):
        MOBO = self.trolley[1]
        RAM = self.trolley[2]
        if RAM is not None and MOBO is not None:
            if RAM[2] == MOBO[5]:
                return True
            else:
                return False
        else:
            return None

    def SeeCompatibiltyCase(self):
        CASE = self.trolley[6]
        MOBO = self.trolley[1]
        if CASE is not None and MOBO is not None:
            if CASE[2] == MOBO[6]:
                return True
            else :
                return False
        else:
            return None
