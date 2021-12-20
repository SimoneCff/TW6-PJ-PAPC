# Basket can have only 8 piece: 0=cpu; 1=mobo; 2=ram; 3=gpu; 4=cooler; 5=psu; 6=case; 7=memory;

class Trolley():
    def __init__(self):
        self.trolley = []
        for i in range(8):
            self.trolley.append(i)

    def InsertCPU(self, cpuid):
        self.trolley.insert(0, cpuid)

    def RemoveCPU(self):
        self.trolley.pop(0)

    def InsertMobo(self, caseid):
        self.trolley.insert(1, caseid)

    def RemoveMobo(self):
        self.trolley.pop(1)

    def InsertRAM(self, ramid):
        self.trolley.insert(2,ramid)

    def removeRAM(self):
        self.trolley.pop(2)

    def


