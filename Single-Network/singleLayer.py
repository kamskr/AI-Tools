import math

class SingleLayer:
    def __init__(self, singleNeurons):
        self.labels = []
        self.weightMatrix = []
        self.biasVector = []
        self.numberOfNeurons = 0
        for neuron in singleNeurons:
            self.labels.append(neuron.label)
            self.weightMatrix.append(neuron.weightVector)
            self.biasVector.append(neuron.bias)
            self.numberOfNeurons = self.numberOfNeurons + 1

    def sigmoid(self, x):
        return 1 / (1 + math.exp(-x))

    def calculateOutput(self, inputVector):
        netVector = []
        y = []

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

        return y

    def train(self, inputVector, learningRate):
        # variables
        y = []
        expectedOutput = []

        # calculate output
        y = self.calculateOutput(inputVector.vector)

        # calculate error signal
        for label in self.labels:
            if label == inputVector.label:
                expectedOutput.append(1)
            else:
                expectedOutput.append(0)
        
        errorSignal = []
        i = 0
        for value in expectedOutput:
            errorSignal.append((float(value) - y[i]) * y[i]  * (float(1)-y[i]))
            i += 1

        # Update weight matrix
        newWeightMatrix = []
        errorN = 0
        for weightVector in self.weightMatrix:
            i = 0
            newWeight = []
            for value in weightVector:
                newWeight.append(value + (learningRate * errorSignal[errorN] * inputVector.vector[i]))
                i = i + 1
            errorN = errorN + 1
            newWeightMatrix.append(newWeight)
        
        self.weightMatrix = newWeightMatrix

        # Update bias vector
        newBiasVector = []
        i = 0
        print(errorSignal)

        for bias in self.biasVector:
            newBiasVector.append(bias - (learningRate * errorSignal[i]))
            i = i + 1

        self.biasVector = newBiasVector
        print(self.biasVector)

    def classify(self, inputVector):
        output = self.calculateOutput(inputVector)
        print(self.biasVector)
        print(output)
        return self.labels[output.index(max(output))]
    

    



    