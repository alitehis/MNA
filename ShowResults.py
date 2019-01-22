from Circuit import *

def printResistors(elements):
    for element in elements:
        print('left = ', element.leftNode)
        print('right = ', element.rightNode) 

def printAddedElements(circuit):
    """
    This method written just for debugging!
    """
    print('---------------------Elements:------------------------')
    print("Resistors:")
    printResistors(circuit.resistors)
    
    print('-----------------capacitors----------------------')
    printResistors(circuit.capacitors)

    print('------------------Inductor-----------------')
    printResistors(circuit.inductors)

    print("-------------------Nodes---------------------")
    for number, node in circuit.nodes.items():
        print("Node number ", number)
        print("Node number: ", node.Number)
        print("connectedResistance: ", node.ResisConnented)
        print('positive indVolt: ', node.PosVolt)
        print("neg IndVolt: ", node.NegVolt)

    print("----------------indep Voltages:----------------")
    for element in circuit.indVolt:
        print("PosTerm: ", element.PosTerm)
        print("negTerm: ", element.NegTerm)

    print('----------------------indep currents-----------------')
    for element in circuit.independentCurrent:
        print('current = ', element.Current)
        print(element.nodes)

    print('-----------------opAmps----------------------')
    for element in circuit.opAmps:
        print('negInput: ', element.NegInput)
        print('posInput: ', element.PosInput)
        print('outNode: ', element.OutNode)


    print('=============================================================')

def printResults(circuit):
    for i in range(1, len(circuit.nodes)):
        print('nodeNumber: ', circuit.nodes[i].Number)
        print(circuit.nodes[i].volt)
    for indVolt in circuit.indVolt:
        print('Independent voltage source:')
        print('     volt: ', indVolt.Voltage)
        print('     posTerm : negTerm ', indVolt.PosTerm, ' : ', indVolt.NegTerm)
        print('     current: ', indVolt.Current)
    for opAmp in circuit.opAmps:
        print('opAmp:')
        print('negIn : posIn ', opAmp.NegInput, ' : ', opAmp.PosInput)
        print('outNode: ', opAmp.OutNode)
        print('cur = ', opAmp.cur)

    for res in circuit.resistors:
        print("Resistors:")
        print("Left : Right", res.leftNode, ' : ', res.rightNode)
        print('resistance: ', res.Resistance)
        print('voltage: ', res.Voltage)
        print('current: ', res.Current)

    for cap in circuit.capacitors:
        print('capacitors:')
        print("Left : Right", cap.leftNode, ' : ', cap.rightNode)
        print('C: ', cap.Capacitance)
        print('voltage: ', cap.Voltage)
        print('current: ', cap.Current)
    
    for ind in circuit.inductors:
        print('inductors:')
        print("Left : Right", ind.leftNode, ' : ', ind.rightNode)
        print('L: ', ind.Inductane)
        print('voltage: ', ind.Voltage)
        print('current: ', ind.Current)