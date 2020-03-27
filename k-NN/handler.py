import PySimpleGUI as sg
import time
import matplotlib.pyplot as plt
from vector import Vector
from csv_parser import CsvParser
from vector_classification import VectorClassification

def calculateFromTestSet(parser, k):
    trainingSet = parser.parseTrainingSet() 
    testSet = parser.parseTestSet()
    testValueList = testSet[0]
    testExpectedResultList = testSet[1]

    classification = VectorClassification(trainingSet)

    start = time.time()
    result = classification.classifyItems(testValueList,k)
    end = time.time()


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
            stringResult += "correct: false \n"


        i += 1

    percent = (float(correct) / float(allTest)) * 100

    # print("accuracy for k =", str(k),": ", str(percent), "%")
    stringResult += "accuracy for k = "
    stringResult += str(k)
    stringResult += ": " 
    stringResult += str(percent)
    stringResult += "% \n"
    stringResult += "total time: "
    stringResult += str(end - start)
    stringResult += "s"
    return stringResult, percent

def pickKRange():
    sg.theme("DarkAmber")
    layout = [
        [sg.Text("Select k range", font=("courier", 20))],
            [sg.Input()],
            [sg.Button("Ok")]]

    window = sg.Window("k-NN Algorithm", layout)
    event, values = window.read() 
    kRange = range(1,int(values[0]))
    window.close()
    return kRange

def printResult(result):
    sg.theme("DarkAmber")
    layout = [
        [sg.Multiline(default_text=result, font=("courier", 20), size=(100,20))] ]
    window = sg.Window("k-NN Algorithm", layout)
    event, values = window.read()  

def graphK(kRange, parser):
    print("plotting")
    plt.plot(kRange,  [float(calculateFromTestSet(parser, k)[1]) for k in kRange])
    plt.show()

    # [calculateFromTestSet(parser, k)[1]