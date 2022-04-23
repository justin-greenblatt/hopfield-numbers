import matplotlib.pyplot as plt
from Experiment import Experiment
from NumberSet import NumberSet
class ErrorExperiment:
    
    def __init__(self, allNumbers, iterations, samples):    
        def setBuild(start,end,replicas):
            outArray = []
            for i in range(start,end,10):
                for s in range(replicas):
                    outArray.append(allNumbers.array[i + s])
                    #print(i+s)
            return outArray

        self.experiment1 = Experiment(NumberSet(setBuild(0, 20, samples)))
        self.experiment2 = Experiment(NumberSet(setBuild(0, 30, samples)))
        self.experiment3 = Experiment(NumberSet(setBuild(0, 40, samples)))
        self.experiment4 = Experiment(NumberSet(setBuild(0, 50, samples)))
        self.experiment5 = Experiment(NumberSet(setBuild(0, 60, samples)))
        self.experiment6 = Experiment(NumberSet(setBuild(0, 70, samples)))
        self.experiment7 = Experiment(NumberSet(setBuild(0, 80, samples)))
        self.experiment8 = Experiment(NumberSet(setBuild(0, 90, samples)))
        self.experiment9 = Experiment(NumberSet(setBuild(0,100, samples)))
        print("Experiment 1 ---------------------")
        self.experiment1.print()
        print("Experiment 2 ---------------------")
        self.experiment2.print()
        print("Experiment 3 ---------------------")
        self.experiment3.print()
        print("Experiment 4 ---------------------")
        self.experiment4.print()
        print("Experiment 5 ---------------------")
        self.experiment5.print()
        print("Experiment 6 ---------------------")
        self.experiment6.print()
        print("Experiment 7 ---------------------")
        self.experiment7.print()
        print("Experiment 8 ---------------------")
        self.experiment8.print()
        print("Experiment 9 ---------------------")
        self.experiment9.print()
    

        


    def plot(self,ax):
        self.experiment1.plot(ax[0][0])
        ax[0][0].set_title(" ".join(list([str(t) for t in range(2)])))
        ax[0][0].set_xticks([])
        #ax[0][0].set_yticks([], minor=True)

        self.experiment2.plot(ax[0][1])        
        ax[0][1].set_title(" ".join(list([str(t) for t in range(3)])))
        ax[0][1].set_xticks([])
        ax[0][1].set_yticks([])
        
        self.experiment3.plot(ax[0][2])
        ax[0][2].set_title(" ".join(list([str(t) for t in range(4)])))
        ax[0][2].set_xticks([])
        ax[0][2].set_yticks([])
        
        self.experiment4.plot(ax[1][0])
        ax[1][0].set_title(" ".join(list([str(t) for t in range(5)])))
        ax[1][0].set_xticks([])
        #ax[1][0].set_yticks([], minor=True)
        
        self.experiment5.plot(ax[1][1])
        ax[1][1].set_title(" ".join(list([str(t) for t in range(6)])))
        ax[1][1].set_xticks([])
        ax[1][1].set_yticks([])
        
        self.experiment6.plot(ax[1][2])
        ax[1][2].set_title(" ".join(list([str(t) for t in range(7)])))
        ax[1][2].set_xticks([])
        ax[1][2].set_yticks([])
        
        self.experiment7.plot(ax[2][0])
        ax[2][0].set_title(" ".join(list([str(t) for t in range(8)])))
        #ax[2][0].set_xticks([], minor=True)
        #ax[2][0].set_yticks([], minor=True)
        
        self.experiment8.plot(ax[2][1])
        ax[2][1].set_title(" ".join(list([str(t) for t in range(9)])))
        #ax[2][1].set_xticks([], minor=True)
        ax[2][1].set_yticks([])
        
        self.experiment9.plot(ax[2][2])
        ax[2][2].set_title(" ".join(list([str(t) for t in range(10)])))
        #ax[2][2].set_xticks([], minor=True)
        ax[2][2].set_yticks([])
