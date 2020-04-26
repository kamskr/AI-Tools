import math

class SingleLayer:
    def __init__(self, *singleNeurons):
        self.labels = []
        self.weightMatrix = []
        self.biasVector = []
        self.numberOfNeurons = 0
        for neuron in singleNeurons:
            self.labels.append(neuron.label)
            self.weightMatrix.append(neuron.weightVector)
            self.biasVector.append(neuron.bias)
            self.numberOfNeurons = self.numberOfNeurons + 1

    def train(self, inputVector, expectedValue):
        # variables
        netVector = []
        y = []
        expectedOutput = []

        # Calculate the net
        n = 0 
        for weightVector in self.weightMatrix:
            singleNetValue = 0
            i = 0
            for value in weightVector:
                singleNetValue = singleNetValue + (value * inputVector[i])
                i = i + 1
            
            singleNetValue = singleNetValue - self.biasVector[n]
            netVector.append(singleNetValue)
            n = n + 1

        # put net through the unipolar sigmoid function
        for value in netVector:
            y.append(self.sigmoid(value))

        # calculate error signal
        for label in self.labels:
            if label == expectedValue:
                expectedOutput.append(1)
            else: 
                expectedOutput.append(0)
        
        errorSignal = []
        i = 0
        for value in expectedOutput:
            errorSignal.append((float(value) - y[i]) * y[i]  * (float(1)-y[i]))

        print(netVector)
        print(y)
        print(expectedOutput)
        print(errorSignal)


    def sigmoid(self, x):
        return 1 / (1 + math.exp(-x))




    