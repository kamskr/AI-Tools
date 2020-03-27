from handler import *

while True:
    sg.theme("DarkAmber")	# Add a touch of color
    # All the stuff inside your window.
    layout = [  
                [sg.Text("Select Training Set", font=("courier", 20))],
                [sg.Input(), sg.FileBrowse()],
                [sg.Text("Select Test Set", font=("courier", 20))],
                [sg.Input(), sg.FileBrowse()],
                [sg.Text("k: ", font=("courier", 20))] ,[sg.Input()],
                [sg.Text("Calculate for 1 vector ", font=("courier", 20))] ,[sg.Input()],
                [sg.Button("Ok"), sg.Button("Cancel"), sg.Button("Graph-k"), sg.Button("ForOneVector")]]

    # Create the Window
    window = sg.Window("k-NN Algorithm", layout)
    # Event Loop to process "events" and get the "values" of the inputs
    files =[]
    pickingFile = True
    k = 0

    graphing = False
    singleVector =[]
    calculateForOne = False

    while pickingFile:
        event, values = window.read()
        if event in (None, "Cancel"):	# if user closes window or clicks cancel
            break
        if values[0] != "" and values[1] != 0:
            files = values
            try: 
                k = int(values[2])
                pickingFile = False
            except:
                print("wrong value of k")
        if event in ("Graph-k"):
            graphing = True
            files = values
            pickingFile = False
        if event in ("ForOneVector"):
            temp = values[3].split(',')
            singleVector = []
            for v in temp:
                singleVector.append(float(v))
            calculateForOne = True
            pickingFile = False


    parser = CsvParser(files[0], files[1])

    if graphing:
        graphK(pickKRange(), parser)
    elif calculateForOne:
        classification = VectorClassification(parser.parseTrainingSet())
        print(singleVector)
        printResult(classification.classify(singleVector,k))
    else:
        printResult(calculateFromTestSet(parser, k)[0])
        
    

    window.close()


