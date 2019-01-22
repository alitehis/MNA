from Node import *
from Component import *


class IndepCur(Component):
    def __init__(self, cur, comeIn: int, comeOut: int, nodes: dict):
        super().__init__(TypeOfComp.IndCur)
        self.__current = cur
        self.__comeInNode = comeIn
        self.__comeOutNode = comeOut
        self.__voltage = None
        self.addToNode(nodes)

    @property
    def Current(self):
        return self.__current

    @property
    def nodes(self):
        return 'comein = ' + str(self.__comeInNode) + 'come out = ' + str(self.__comeOutNode)

    def addToNode(self, nodes: dict):
        comeInNode = checkExistanceOfNode(self.__comeInNode, nodes)
        comeInNode.addEntryCurrent(self.__current)

        comeOutNode = checkExistanceOfNode(self.__comeOutNode, nodes)
        comeOutNode.addComeOutCurrent(self.__current)

    def setVoltage(self):
        self.__voltage = abs(self.comeInNode.voltage - self.comeOutNode.voltage)
