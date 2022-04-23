from random import randint
import editdistance
from NumberSet import NumberSet

class Number:
    def __init__(self, data, label):
        self.data = data
        self.label = label

    def __str__(self): 
        out = ""
        for a in range(0,len(self.data),10):
            out += self.data[a:a+10].replace('0',"  ").replace('1', chr(0x1f7e5)) + '\n' 
        return out

    def getMutant(self, pct = 0.1):

        mutant = self.data
        positions = []

        if pct < 1:
            for i in range(round(len(self.data)*pct)):

                randomIndex = randint(0, len(self.data) - 1)
                while randomIndex in positions:
                    randomIndex = randint(0, len(self.data) - 1)

                if mutant[randomIndex] == '1':
                    mutant = mutant[:randomIndex] + '0' + mutant[randomIndex + 1:]
                else:
                    mutant = mutant[:randomIndex] + '1' + mutant[randomIndex + 1:]

        return Number(mutant, self.label)

    def closestTo(self,group):
        e = [[editdistance.eval(self.data, other.data),other] for other in group.array]
        neighbor = sorted(e, key = lambda x: x[0])[0]
        return neighbor