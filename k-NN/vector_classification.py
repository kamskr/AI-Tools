from collections import Counter

class VectorClassification:
    def __init__(self, trainingSet):
        self.trainingSet = trainingSet

    def classify(self, testVector, accuracy):
        distanceList = []
        for compareVector in self.trainingSet:
            distanceList.append(compareVector.calculateDistance(testVector))

        distanceList.sort(key=lambda tup: tup[0])

        listOfKResults = distanceList[:accuracy]
        
        extractedKeys = [x[1] for x in listOfKResults]
        
        return  testVector ,max(set(extractedKeys), key=extractedKeys.count)

 
    def classifyItems(self, testSet, accuracy):
        result = [] # tuple: [(vector: []), (result)]
        for vector in testSet:
            result.append((self.classify(vector,accuracy)))

        return result
        

        
