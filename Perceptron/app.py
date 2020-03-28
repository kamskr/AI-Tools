from handler import *

while True:
    sg.theme("DarkAmber")	
    layout = [  
                [sg.Text("Select Training Set", font=("courier", 20))],
                [sg.Input(), sg.FileBrowse()],
                [sg.Text("Select Test Set", font=("courier", 20))],
                [sg.Input(), sg.FileBrowse()],
                [sg.Text("learning rate: ", font=("courier", 20))] ,[sg.Input()],
                [sg.Text("max iterations: ", font=("courier", 20))] ,[sg.Input()],
                [sg.Text("threshold E: ", font=("courier", 20))] ,[sg.Input()],
                [sg.Text("Calculate for 1 vector ", font=("courier", 20))] ,[sg.Input()],
                [sg.Button("Ok"), sg.Button("Cancel"), sg.Button("ForOneVector")]]

    # Create the Window
    window = sg.Window("Perceptron", layout)

    files =[]
    pickingFile = True
    learningRate = 0
    maxIterations = 0

    singleVector =[]
    calculateForOne = False
    thresholdE = 0

    while pickingFile:
        event, values = window.read()
        if event in (None, "Cancel"):	# if user closes window or clicks cancel
            break
        if values[0] != "" and values[1] != 0 and values[2] != 0 and values[3] != 0:
            files = values
            try: 
                learningRate = float(values[2])
                pickingFile = False
                maxIterations = int(values[3])
                thresholdE = int(values[4])

            except:
                print("wrong value of learning rate")
        
        if event in ("ForOneVector"):
            temp = values[5].split(',')
            singleVector = []
            for v in temp:
                singleVector.append(float(v))
            calculateForOne = True
            pickingFile = False


    parser = CsvParser(files[0], files[1])

    if calculateForOne:
        classification = VectorClassification(parser.parseTrainingSet())
        print(singleVector)
        classification.train(learningRate, thresholdE, maxIterations)
        printResult(classification.classify(singleVector))
    else:
        printResult(calculateFromTestSet(parser, learningRate, thresholdE, maxIterations)[0])
        print(calculateFromTestSet(parser, learningRate, 99, maxIterations)[0])
    window.close()


