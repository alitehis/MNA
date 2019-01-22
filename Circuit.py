from Resistance import *
from OpAmp import *
from IndepVoltage import *
from Node import *
from IndepCur import *
from Capacitor import *
from Solve import *
from Capacitor import *
from Inductor import *
import numpy as np
from typing import List, Dict, Optional
from time import sleep
import math
import cmath


class Circuit():
    def __init__(self):
        self.nodes: Dict[int, Node] = {}
        self.resistors: List[Resistance] = []
        self.opAmps: List[OpAmp] = []
        self.indVolt: List[IndepVolt] = []
        self.independentCurrent = []
        self.capacitors: List[Capacitor] = []
        self.inductors: List[Inductor] = []
        self.__w: float = 0
        self.__theta: float = 0.0
        self.__max: float = 0.0
        self.__alternate = False

    def addResistor(self, rightNode: int, leftNode: int, resistance: int):
        res = Resistance(resistance, leftNode, rightNode, self.nodes)
        self.resistors.append(res)

    def addOpAmp(self, negNode: int, posNode: int, outNode: int):
        newOpAmp = OpAmp(negNod, posNode, outNode)
        self.opAmps.append(newOpAmp)

    def addIndVolt(self, voltage, posTerm: int, negTerm: int):
        phasorVoltage: complex = 0
        
        if type(voltage) is str:
            self.__alternate = True
            phasorVoltage = self.convertToPhasor(voltage)

            print("Max:", self.__max)
            print("theta: ", self.__theta)
            print("W: ", self.__w)
            print("phasor volt:", phasorVoltage)

            newIndVolt = IndepVolt(phasorVoltage, posTerm, negTerm, self.nodes)
        else:
            newIndVolt = IndepVolt(voltage, posTerm, negTerm, self.nodes)
        self.indVolt.append(newIndVolt)

    def addIndCur(self, comeInNode, comeOutNode, current):
        phasorCurrent: complex = 0
        if type(current) is str:
            self.__alternate = True
            phasorCurrent = self.convertToPhasor(current)

            print("Max:", self.__max)
            print("theta: ", self.__theta)
            print("W: ", self.__w)
            print("phasor cur:", phasorCurrent)

            newIndCur = IndepCur(phasorCurrent, comeInNode, comeOutNode, self.nodes)
        else:
            newIndCur = IndepCur(current, comeInNode, comeOutNode, self.nodes)
        self.independentCurrent.append(newIndCur)

    def addOpAmp(self, negInput, posInput, outNode):
        newOpAmp = OpAmp(negInput, posInput, outNode)
        self.opAmps.append(newOpAmp)

    def addCapacitor(self, capacitance, left, right):
        newCapacitor = Capacitor(capacitance, self.__w, left, right, self.nodes)
        self.capacitors.append(newCapacitor)

    def addInductor(self, inductance, left, right):
        newInductor = Inductor(inductance, self.__w, left, right, self.nodes)
        self.inductors.append(newInductor)

    def convertToPhasor(self, source):

        if "sin" in source:
            source = source.replace("sin", "cos")
            self.__theta -= 90.0
 
        alternatePart = source.split("cos")[1][1:-1]

        self.__max = float(source.split("cos")[0])
        self.__w = float(alternatePart.split("t")[0])
        self.__theta += float(alternatePart.split("t")[1])

        radiansTheta = math.radians(self.__theta)

        phasorSource = self.__max * cmath.exp(radiansTheta * 1j)
        phasorSource = round(phasorSource.real, 3) + round(phasorSource.imag, 3) * 1j

        return phasorSource 

    def calc(self):
        m = len(self.indVolt) + len(self.opAmps)
        n = len(self.nodes) - 1 #ignoring 0 node
        solver = Solve(m, n)
        solver.generateA(self.nodes, 
                self.inductors + self.capacitors + self.resistors,
                self.indVolt, self.independentCurrent, self.opAmps)
        solver.generateZ(self.nodes, self.indVolt)
        results = solver.solveCircut()
        print(results)
        self.addResultsToCircut(results)

    def addResultsToCircut(self, results):
        numberOfNodes = len(self.nodes)
        for i in range(1, numberOfNodes):
            self.nodes[i].volt = results[i - 1][0]

        numberOfIndVolts = len(self.indVolt)
        for i in range(0, numberOfIndVolts):
            self.indVolt[i].cur = results[i + numberOfNodes - 1][0]
        
        numberOfOpAmps = len(self.opAmps)
        for i in range(0, numberOfOpAmps):
            self.opAmps[i].cur = results[i + numberOfNodes + numberOfIndVolts - 1][0]

        numbeOfResistors = len(self.resistors)
        for i in range(0, numbeOfResistors):
            self.resistors[i].setVoltageAndCur(
                self.nodes[self.resistors[i].leftNode], self.nodes[self.resistors[i].rightNode]
                )
        
        numberOfCapacitors = len(self.capacitors)
        for i in range(0, numberOfCapacitors):
            self.capacitors[i].setVoltageAndCur(
                self.nodes[self.capacitors[i].leftNode], self.nodes[self.capacitors[i].rightNode]
            )

        numberOfInductors = len(self.inductors)
        for i in range(0, numberOfInductors):
            self.inductors[i].setVoltageAndCur(
                self.nodes[self.inductors[i].leftNode], self.nodes[self.inductors[i].rightNode]
            )
