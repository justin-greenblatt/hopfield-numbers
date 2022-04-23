from HopfieldNetwork import HopfieldNetwork
from itertools import cycle
from NumberSet import NumberSet
from random import randint

class Experiment:
    def __init__(self, learnSet, evalSet = None, evalMutationPct = 0.1, lenEvalSet = 30, evalIterations = 500, learnReplicas = 1):
        
        self.network = HopfieldNetwork(100)
        
        self.learnSet = learnSet
        
        self.network.learn(learnSet)
        
        self.evalSet = NumberSet([])

        self.outputSets = []


        if evalSet != None:
            self.evalSet = evalSet
        else:
            if lenEvalSet > len(learnSet.array):

                for i,j in zip(cycle(learnSet.array),range(lenEvalSet)):
                    self.evalSet.append(i.getMutant())
            else:
                for i in range(lenEvalSet):
                    self.evalSet.append(self.learnSet.array[randint(0,len(learnSet.array) - 1)].getMutant())
        for i in self.evalSet.array: 
            self.outputSets.append(self.network.evaluate(i,evalIterations))
        
        self.errors = [sum(list([g.stats["idArray"][n] for g in self.outputSets])) for n in range(evalIterations)]
        for i in self.outputSets:
            i.array.insert(0,self.learnSet.array[i.array[1].label * learnReplicas])


    def plot(self, axis):
        for i in self.outputSets:
            axis.plot(i.stats["distanceArray"], color = "grey")
        axis.plot(self.errors, color = 'black')
    
    def print(self):
        for i in self.outputSets:
            i.print()
