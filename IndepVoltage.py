from Node import *
from Component import *


class IndepVolt(Component):
    def __init__(self, voltage: int, posTerm: int, negTerm: int, nodes: dict):
        super().__init__(TypeOfComp.IndVolt)
        self.__voltage = voltage
        self.__posTerm = posTerm
        self.__negTerm = negTerm
        self.cur = None
        self.addToNode(nodes)

    @property
    def Voltage(self):
        return self.__voltage

    def VoltageSetter(self, voltage):
        self.__voltage = voltage

    @property
    def Current(self):
        return self.cur

    @property
    def PosTerm(self):
        return self.__posTerm

    @property
    def NegTerm(self):
        return self.__negTerm

    def addToNode(self, nodes: dict):
        posTerm = checkExistanceOfNode(self.__posTerm, nodes)
        posTerm.addPosVoltage(self.__voltage)

        negTerm = checkExistanceOfNode(self.__negTerm, nodes)
        negTerm.addNegVoltage(self.__voltage)
