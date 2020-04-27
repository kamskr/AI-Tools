import random

class SingleNeuron:
    def __init__(self, label):
        self.label = label
        self.weightVector = []
        for _ in range(26):
            # self.weightVector.append(random.uniform(0.0,1.0))
            self.weightVector.append(1)
        # self.bias = random.uniform(0.0,1.0)
        self.bias = 1

        
