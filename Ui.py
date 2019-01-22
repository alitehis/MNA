from Circuit import *
import ShowResults


if __name__ == '__main__':
    circut = Circuit()
    while True:
        element = input().split()
        if element[0] == 'R':
            leftNode = int(element[1])
            rightNode = int(element[2])
            resistance = float(element[3])
            circut.addResistor(rightNode, leftNode, resistance)
        elif element[0] == 'IV':
            posTerm = int(element[1])
            negTerm = int(element[2])
            try:
                voltage = float(element[3])
            except ValueError:
                voltage = element[3]
                print("Alternate source")
            circut.addIndVolt(voltage, posTerm, negTerm)
        elif element[0] == 'IC':
            comeIn = int(element[1])
            comeOut = int(element[2])
            try:
                cur = float(element[3])
            except ValueError:
                cur = element[3]
                print('Aternate  source')
            circut.addIndCur(comeIn, comeOut, cur)

        elif element[0] == 'OA':
            posInputNode = int(element[1])
            negInputNode = int(element[2])
            outInputNode = int(element[3])
            circut.addOpAmp(negInputNode, posInputNode, outInputNode)
        
        elif element[0] == 'C':
            if not circut._Circuit__alternate:
                raise ValueError("There isn't any source!")
            left = int(element[1])
            right = int(element[2])
            capacitance = float(element[3])
            circut.addCapacitor(capacitance, left, right )

        elif element[0] == 'L':
            if not circut._Circuit__alternate:
                raise ValueError("There isn't any source!")
            left = int(element[1])
            right = int(element[2])
            inductance = float(element[3])
            circut.addInductor(inductance, left, right)

        elif element[0] == 'calculate':
            circut.calc()
            ShowResults.printAddedElements(circut)
            ShowResults.printResults(circut)
            break
        else:
            break
