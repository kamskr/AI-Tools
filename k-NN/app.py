from vector import Vector
from csv_parser import CsvParser
from vector_classification import VectorClassification


parser = CsvParser("./set/iris.data", "./set/iris.test.data")

trainingSet = parser.parseTrainingSet() 
testSet = parser.parseTestSet()
testValueList = testSet[0]
testExpectedResultList = testSet[1]


classification = VectorClassification(trainingSet)

result = classification.classifyItems(testValueList,5)

i = 0
for v in result:
    if testExpectedResultList[i] == v[1]:
        print(v, " correct: true")
    else:
        print(v, " correct: false")
    i += 1
    







