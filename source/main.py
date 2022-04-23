import matplotlib.pyplot as plt
from ErrorExperiment import ErrorExperiment
from Number import Number
from NumberSet import NumberSet

DATA = "dataBig.txt"

handler = open(DATA)
allNumbers = NumberSet(list([Number(t.replace("\n",""), i) for t,i in zip(handler.read().split("\n\n"),[c for d in [[a for b in range(10)] for a in range(10)] for c in d])]))
handler.close()

for i in [1]:
    fig, axs = plt.subplots(3,3)
    experiment = ErrorExperiment(allNumbers,500,i)
    fig.suptitle("Hopfield Network performance using {} learning samples per digit".format(str(i)))
    experiment.plot(axs)
    plt.show()