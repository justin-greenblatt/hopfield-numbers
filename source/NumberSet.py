from math import ceil, floor

class NumberSet:
    def __init__(self,numberArray):
        self.array = numberArray
        self.stats = {}
        
    def append(self,x):
        self.array.append(x)

    def print(self, step = 10, sep = "\u2588\u2588"):
        for i in range(ceil(len(self.array)/step)):
            arraySlice = self.array[i * step : (i + 1) * step]
            for j in range(10):
                if j == 0:
                    casset = sep * 9
                    print(sep + casset.join(list([str(s.label) + ' ' + sep for s in arraySlice])) + casset)
                print(sep + sep.join(list([str(a).split('\n')[j] for a in arraySlice if str(a)])) + sep)