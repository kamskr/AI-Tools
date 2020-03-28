import PySimpleGUI as sg
import time
import matplotlib.pyplot as plt
from vector import Vector
from csv_parser import CsvParser
from vector_classification import VectorClassification

def calculateFromTestSet(parser, learningRate, thresholdE, maxIterations):
    trainingSet = parser.parseTrainingSet() 
    testSet = parser.parseTestSet()
    testValueList = testSet[0]
    testExpectedResultList = testSet[1]

    classification = VectorClassification(trainingSet)
    start = time.time()
    classification.train(learningRate, thresholdE, maxIterations)
    end = time.time()
    trainingTime = str(end - start)

    start = time.time()
    result = classification.classifyItems(testValueList)
    end = time.time()
    testingTime = str(end - start)

    i = 0
    correct = 0
    allTest = 0
    stringResult = ""

    for v in result:
        allTest += 1
        if testExpectedResultList[i] == v[1]:
            # print(v," expected class:", testExpectedResultList[i]   ,"correct: true")
            stringResult += str(v)
            stringResult += " expected class: "
            stringResult += str(testExpectedResultList[i])
            stringResult += "correct: true \n"
            correct += 1
        else:
            # print(v," expected class:", testExpectedResultList[i], "correct: false")
            stringResult += str(v)
            stringResult += " expected class: "
            stringResult += str(testExpectedResultList[i])
            stringResult += " correct: false \n"

        i += 1

    percent = (float(correct) / float(allTest)) * 100

    stringResult += "accuracy for learning rate ="
    stringResult += str(learningRate)
    stringResult += ": " 
    stringResult += str(percent)
    stringResult += "% \n"
    stringResult += "Training time: "
    stringResult += trainingTime
    stringResult += "s"
    stringResult += "Testing time: "
    stringResult += testingTime
    stringResult += "s"
    return stringResult, percent

# def pickKRange():
#     sg.theme("DarkAmber")
#     layout = [
#         [sg.Text("Select k range", font=("courier", 20))],
#             [sg.Input()],
#             [sg.Button("Ok")]]

#     window = sg.Window("k-NN Algorithm", layout)
#     event, values = window.read() 
#     kRange = range(1,int(values[0]))
#     window.close()
#     return kRange

def printResult(result):
    sg.theme("DarkAmber")
    layout = [
        [sg.Multiline(default_text=result, font=("courier", 20), size=(100,20))] ]
    window = sg.Window("Perceptron result", layout)
    event, values = window.read()  

# def graphK(kRange, parser):
#     print("plotting")
#     plt.plot(kRange,  [float(calculateFromTestSet(parser, k)[1]) for k in kRange])
#     plt.show()

    # [calculateFromTestSet(parser, k)[1]