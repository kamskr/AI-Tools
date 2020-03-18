import csv 
from vector import Vector

class CsvParser:
    def __init__(self, traingingSetFile, testSetFile):
        self.trainingSetFile = traingingSetFile
        self.testSetFile = testSetFile

    def parseTrainingSet(self):
        trainingSet = []
        with open(self.trainingSetFile, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                vector = []
                name = ""
                for v in row:
                    try:
                        vector.append(float(v))
                    except ValueError:
                        name = v
                trainingSet.append(Vector(name, vector))
        return trainingSet
                
    def parseTestSet(self):
        testVectorList = []
        expectedResultList = []
        with open(self.testSetFile, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                vector = []
                expectedResult = ""
                for v in row:
                    try:
                        vector.append(float(v))
                    except ValueError:
                        expectedResult = v
                testVectorList.append(vector)
                expectedResultList.append(expectedResult)
        return testVectorList, expectedResultList


