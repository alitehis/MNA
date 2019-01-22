from Resistance import *


class Capacitor(Resistance):
    def __init__(self, capacitance: int, w: int, left: int, right: int, nodes):
        super().__init__(1/(w * 1j * capacitance), left, right, nodes)
        self.__capacitance = capacitance

    @property
    def Capacitance(self):
        return self.__capacitance
