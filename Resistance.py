from Node import *
from Circuit import *
from typing import Union


class Resistance(Component):
    def __init__(self, resistance: Union[int, complex], left: int, right: int, nodes):
        Component.__init__(self, TypeOfComp.Res)
        self.__resistance: int = resistance
        self.__left = left
        self.__right = right
        self.__cur = 0.0
        self.__voltage = 0.0
        self.addToNode(nodes)

    def addToNode(self, nodes):
        leftObject = checkExistanceOfNode(self.__left, nodes)
        leftObject.addResistance(self.__resistance)

        rightObject = checkExistanceOfNode(self.__right, nodes)
        rightObject.addResistance(self.__resistance)

    @property
    def Resistance(self):
        return self.__resistance

    @property
    def Voltage(self):
        return self.__voltage

    @property
    def Current(self):
        return self.__cur

    @property
    def SideNodes(self):
        return 'Left : ' + str(self.__left) + ' Right : ' + str(self.__right)

    @property
    def rightNode(self):
        return self.__right

    @property
    def leftNode(self):
        return self.__left

    def setVoltageAndCur(self, left: Node, right: Node):
        """
            We assumeed that current comes from left to right
        """
        self.__voltage = left.volt - right.volt
        self.__cur = self.__voltage/self.__resistance
