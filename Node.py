from Component import *


class Node(Component):
    def __init__(self, number: int):
        super().__init__(TypeOfComp.Node)
        self.resisConnected = []
        self.__comeInCurrents = []
        self.__comeOutCurrents = []
        self.__number = number
        self.__posVoltages = []
        self.__negVoltages = []
        self.volt = 0.0 + 0.0j

    @property
    def Number(self):
        return self.__number

    @property
    def ResisConnented(self):
        return self.resisConnected

    @property
    def PosVolt(self):
        return self.__posVoltages

    @property
    def NegVolt(self):
        return self.__negVoltages

    @property
    def comeInCurrents(self):
        return self.__comeInCurrents

    @property
    def comeOutCurrents(self):
        return self.__comeOutCurrents

    def addResistance(self, resistance: int):
        self.resisConnected.append(resistance)
    
    def addEntryCurrent(self, current):
        self.comeInCurrents.append(current)

    def addComeOutCurrent(self, current):
        self.comeOutCurrents.append(current)

    def addPosVoltage(self, voltage):
        self.__posVoltages.append(voltage)
        
    def addNegVoltage(self, voltage):
        self.__negVoltages.append(voltage)
