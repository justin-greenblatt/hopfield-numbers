from random import randint
from Number import Number
from NumberSet import NumberSet

class HopfieldNetwork:
    def __init__(self,nodes):
        self.nNodes = nodes
        self.evalGroups = []
        self.initialize = False
    def __len__(self):
         return self.nNodes


    def learn(self, learnSet):
        self.learnSet = learnSet
        self.initialize = True
        weightMatrix = []
        
        for i in range(len(self)):
            weightMatrix.append([])
            for j in range(len(self)):
                colI = [s.data[i] for s in learnSet.array]
                colJ = [s.data[j] for s in learnSet.array]
                weightMatrix[i].append(sum(list([1 if Ci == Cj else -1 for Ci,Cj in zip(colI,colJ)])))


        self.weights = weightMatrix



    def evaluate(self,evalNumber, iterations = 100, multWeights = (1,0)):
        evalString = evalNumber.data
        def s(character):
            if character == '0':
                return multWeights[1]
            else: 
                return multWeights[0]

        randomIndex = None
        distanceArray = []
        idArray = []
        
        if self.initialize and len(evalString) == self.nNodes:

            for i in range(iterations):
                verbose = ""

                if randomIndex == None:
                    randomIndex = randint(0,len(self) - 1)

                else:
                    r = randint(0,len(self) - 1)
                    while r == randomIndex:
                        r = randint(0,len(self) - 1)
                    randomIndex = r
                
                ListR = list([s(evalString[z]) * self.weights[randomIndex][z] for z in range(len(self)) if z != randomIndex])
        
                sumR = sum(ListR)

                out = None
                if sumR >= 0:
                    out = evalString[:randomIndex] + '1' + evalString[randomIndex + 1:]
                else:
                    out = evalString[:randomIndex] + '0' + evalString[randomIndex + 1:]

                evalString = out
                newNumber = Number(evalString,evalNumber.label)
                d,match = newNumber.closestTo(self.learnSet)
                distanceArray.append(d)
                if match.label == evalNumber.label:
                    idArray.append(0)
                else:
                    idArray.append(1)
            outGroup = NumberSet([evalNumber,Number(evalString,evalNumber.label)])
            outGroup.stats["distanceArray"] = distanceArray
            outGroup.stats["idArray"] = idArray
            return outGroup

        else:
            print("Error")