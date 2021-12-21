# Basket can have only 8 piece: 0=cpu; 1=mobo; 2=ram; 3=gpu; 4=cooler; 5=psu; 6=case; 7=memory;

class Trolley():
    def __init__(self):
        self.trolley = [7]

    def InsertCPU(self, cpuid):
        self.trolley[0] = cpuid

    def RemoveCPU(self):
        self.trolley[0] = False

    def InsertMobo(self, caseid):
        self.trolley[1] = caseid

    def RemoveMobo(self):
        self.trolley[1] = False

    def InsertRAM(self, ramid):
        self.trolley[2] = ramid

    def removeRAM(self):
        self.trolley[2] = False

    def returnList(self):
        return self.trolley
