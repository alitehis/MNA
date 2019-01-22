from Component import *

class OpAmp(Component):
    def __init__(self, negNode: int, posNode: int, outNode: int):
        super().__init__(TypeOfComp.OpAmp)
        self.__negNodeNumber = negNode
        self.__posNodeNum = posNode
        self.__outNodeNum = outNode
        self.cur = None

    @property
    def NegInput(self):
        return self.__negNodeNumber
    
    @property
    def PosInput(self):
        return self.__posNodeNum

    @property
    def OutNode(self):
        return self.__outNodeNum
