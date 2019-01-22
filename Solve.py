import numpy as np
import numpy.linalg as linearAlg
from Circuit import *
from Node import *
from Resistance import *


class Solve():
    def __init__(self, m, n):
        """
        n = number of nodes(without 0)
        m = number of independent voltage sources and opAmp
        The equation is AX = Z
        The A matrix consist of 4 matrixes:
            [g, b]
            [c, d]
            g -> n * n
            b -> n * m
            c -> m * n
            d -> m * m
        The X matrix consist of 2 matrix:
            [v] -> n * 1
            [j] -> m * 1
        The Z matrix consist of 2 marixes:
            [i] -> n * 1
            [e] - m * 1
        """
        print(n, ' ', m)

        self.__A = np.zeros((m + n, m + n) ,dtype=np.complex_)
        self.__g = np.zeros((n, n) ,dtype=np.complex_)
        self.__b = np.zeros((n, m) ,dtype=np.complex_)
        self.__c = np.zeros((m, n) ,dtype=np.complex_)
        self.__d = np.zeros((m, m) ,dtype=np.complex_)

        self.__X = np.zeros((n + m, 1) ,dtype=np.complex_)
        self.__v = np.zeros((n, 1) ,dtype=np.complex_)
        self.__j = np.zeros((m, 1) ,dtype=np.complex_)

        self.__Z = np.zeros((n + m, 1) ,dtype=np.complex_)
        self.__i = np.zeros((n, 1) ,dtype=np.complex_)
        self.__e = np.zeros((m, 1) ,dtype=np.complex_)

    def generateG(self, nodes, resistors):
        for i in range(1, len(nodes)):
            print(nodes[i].ResisConnented)
            sumr = 0
            for resistor in nodes[i].ResisConnented:
                sumr += 1/resistor
            self.__g[i-1][i-1] = sumr
        for res in resistors:
            left = res.leftNode - 1
            right = res.rightNode - 1
            
            if right == -1 or left == -1:
                continue
            
            self.__g[left][right] += -1/res.Resistance
            self.__g[right][left] += -1/res.Resistance
        print('G = ', self.__g)

    def generateB(self, indVolts, opAmps):
        numberOfIndVolts = len(indVolts)
        for i in range(0, numberOfIndVolts):
            posTerm = indVolts[i].PosTerm - 1
            negTerm = indVolts[i].NegTerm - 1
            import sys
            print(f"indVolts: {indVolts}, posTerm: {posTerm}", file=sys.stderr)
            if posTerm != -1:
                self.__b[posTerm][i] = 1
            if negTerm != -1:
                self.__b[negTerm][i] = -1

        columnOfFirstOpAmp = numberOfIndVolts
        print('opAms: ', len(opAmps))
        for i in range(0, len(opAmps)):
            outNodeIndex = opAmps[i].OutNode - 1
            print('outNodeIndex: ', outNodeIndex)
            if outNodeIndex != -1:
                self.__b[outNodeIndex][columnOfFirstOpAmp + i] = 1
        print('B = ', self.__b)

    def generateC(self, indVolts, opAmps):
        numberOfIndVolts = len(indVolts)
        for i in range(0, numberOfIndVolts):
            posTerm = indVolts[i].PosTerm - 1
            negTerm = indVolts[i].NegTerm - 1
            if posTerm != -1:
                self.__c[i][posTerm] = 1
            if negTerm != -1:
                self.__c[i][negTerm] = -1
        rowOfFirstOpAmp = numberOfIndVolts
        for i in range(0, len(opAmps)):
            negInput = opAmps[i].NegInput - 1
            posInput = opAmps[i].PosInput - 1
            if negInput != -1:
                self.__c[rowOfFirstOpAmp + i][negInput] = -1
            if posInput != -1:
                self.__c[rowOfFirstOpAmp + i][posInput] = 1
        print('C = ')
        print(self.__c)
        print('D = ')
        print(self.__d)

    def generateA(self, nodes, resistors, indVolts, indCurs, opAmps):
        self.generateG(nodes, resistors)
        self.generateB(indVolts, opAmps)
        self.generateC(indVolts, opAmps)
        leftSide = np.concatenate((self.__g, self.__c))
        rightSide = np.concatenate((self.__b, self.__d))
        self.__A = np.hstack((leftSide, rightSide))
        print('A = ')
        print(self.__A)

    def generateI(self, nodes):
        for i in range(1, len(nodes)):
            nodeRow = i - 1
            self.__i[nodeRow][0] = sum(nodes[i].comeInCurrents) - sum(nodes[i].comeOutCurrents)
            print('NodeRow: ', nodeRow)
            print(nodes[i].comeInCurrents)
            print(nodes[i].comeOutCurrents)
        return self.__i

    def generateE(self, indepVolts):
        for i in range(0, len(indepVolts)):
            self.__e[i][0] = indepVolts[i].Voltage
        return self.__e

    def generateZ(self, nodes, indepVolts):
        downSide = self.generateE(indepVolts)
        upSide = self.generateI(nodes)
        print('upSide: ')
        print(upSide)
        print('downSide: ')
        print(downSide)
        self.__Z = np.concatenate((upSide, downSide))
        print('Z = ', self.__Z)
    
    def solveCircut(self):
        return linearAlg.solve(self.__A, self.__Z)
