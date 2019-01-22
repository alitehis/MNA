from enum import Enum
import Node


class TypeOfComp(Enum):
    Res = "Resistance"
    Node = "Node"
    OpAmp = "OpAmp"
    IndVolt = "Independent voltage"
    IndCur = "Independent Current"

class Component():
    def __init__(self, type: TypeOfComp):
        self.__voltage: int = 0
        self.__charge: int = 0
        self.__type = type

    @property
    def Type(self):
        return self.__type

def checkExistanceOfNode(nodeNumber, nodes: dict):
    if nodeNumber in nodes:
        node = nodes[nodeNumber]
    else:
        node = Node.Node(nodeNumber)
        nodes[nodeNumber] = node
    return node
