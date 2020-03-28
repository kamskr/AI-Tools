from collections import Counter
import random

class VectorClassification:
    def __init__(self, trainingSet):
        self.trainingSet = trainingSet
        # generating random bias and weight vector
        self.weightVector = []
        for i in trainingSet[0].vector:
            self.weightVector.append(random.uniform(-4.0,4.0))
        self.bias = random.uniform(-2.0, 2)
        # get unique values of class name in training set
        self.classNames = list({vector.name for vector in self.trainingSet})
        print(self.classNames)

    def train(self, learningRate, thresholdE, maxIterations):
        training = True
        iteration = 0
        while training:
            print("training iteration: ", str(iteration))
            iterationError = 0
            for vector in self.trainingSet:
                i = 0
                d = 1 if vector.name == self.classNames[0] else 0
                net = 0
                for value in vector.vector:
                    net = net + (value * self.weightVector[i])
                    i = i + 1

                net = net - self.bias
                if net < 0:
                    y = 0
                else:
                    y = 1
                
                self.deltaRule(vector.vector, d, y, learningRate)
                iterationError = iterationError + abs(d - y)
            iteration = iteration + 1
            if iteration >= maxIterations or iterationError <= thresholdE:
                print(iteration)
                training = False

    def deltaRule(self, vector, d, y, learningRate):
        i = 0
        for value in self.weightVector:
            self.weightVector[i] = self.weightVector[i] + (vector[i] * float(learningRate) * (d - y))
            i = i + 1
        self.bias = self.bias - (learningRate * (d - y))

    def classify(self, testVector):
        i = 0
        net = 0
        for value in testVector:
            net = net + (value * self.weightVector[i])
            i = i + 1
        net = net - self.bias
        if net < 0:
            return testVector, self.classNames[1]
        else:
            return testVector, self.classNames[0]
 
    def classifyItems(self, testSet):
        result = [] # tuple: [(vector: []), (result)]
        for vector in testSet:
            result.append((self.classify(vector)))

        return result
        

        
