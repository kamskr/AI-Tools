from handler import *

# parser = CsvParser("./data/perceptron.data", "./data/perceptron.test.data")
# print(calculateFromTestSet(parser, 1, 99, 1)[0])

while True:
    sg.theme("DarkAmber")	
    layout = [  
                [sg.Text("Select Training Set", font=("courier", 20))],
                [sg.Input(), sg.FileBrowse()],
                [sg.Text("Select Test Set", font=("courier", 20))],
                [sg.Input(), sg.FileBrowse()],
                [sg.Text("learning rate: ", font=("courier", 20))] ,[sg.Input()],
                [sg.Text("Calculate for 1 vector ", font=("courier", 20))] ,[sg.Slider(0,1)],
                [sg.Button("Ok"), sg.Button("Cancel"), sg.Button("Graph-learning-rate"), sg.Button("ForOneVector")]]

    # Create the Window
    window = sg.Window("Perceptron", layout)

    # files =[]
    # pickingFile = True
    # learningRate = 0

    # graphing = False
    # singleVector =[]
    # calculateForOne = False

    # while pickingFile:
    #     event, values = window.read()
    #     if event in (None, "Cancel"):	# if user closes window or clicks cancel
    #         break
    #     if values[0] != "" and values[1] != 0:
    #         files = values
    #         try: 
    #             learningRate = float(values[2])
    #             pickingFile = False
    #         except:
    #             print("wrong value of learning rate")
    #     if event in ("Graph-learning-rate"):
    #         graphing = True
    #         files = values
    #         pickingFile = False
    #     if event in ("ForOneVector"):
    #         temp = values[3].split(',')
    #         singleVector = []
    #         for v in temp:
    #             singleVector.append(float(v))
    #         calculateForOne = True
    #         pickingFile = False


    # parser = CsvParser(files[0], files[1])

    # if graphing:
    #     # graphK(pickKRange(), parser)
    # elif calculateForOne:
    #     classification = VectorClassification(parser.parseTrainingSet())
    #     print(singleVector)
    #     printResult(classification.classify(singleVector,k))
    # else:
    # printResult(calculateFromTestSet(parser, learningRate)[0])
        
    

    # window.close()


