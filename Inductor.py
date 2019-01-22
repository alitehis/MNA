from Resistance import *


class Inductor(Resistance):
    def __init__(self, inductance: int, w: int, left: int, right: int, nodes):
        super().__init__(w * 1j * inductance, left, right, nodes)
        self.__inductance = inductance

    @property
    def Inductane(self):
        return self.__inductance
