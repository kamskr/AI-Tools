import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import theme
from handler import Handler
from parser import Parser

class MainMenu:
    def __init__(self):
        directories = {
                "English": "data/lang/English/",
                "German": "data/lang/German/",
                "Polish": "data/lang/Polish/"
        }
        self.handler = Handler(directories)
        self.initializeMenu()

    def initializeMenu(self):
        while True:
            sg.theme("DarkTeal2")	
            print("init")
            layout = [  
                    [sg.Text("number of iterations: ", font=("courier", 20))] ,[sg.Input()],
                    [sg.Text("learning rate: ", font=("courier", 20))] ,[sg.Slider(range=(0.0, 1.0), orientation='h', resolution=.1, size=(40, 20), default_value=0.5)],
                    [sg.Button("Train"),sg.Button("Graph"), sg.Button("Cancel")]]
    
            window = sg.Window("Single-Layer Network", layout)
            event, values = window.read()
            if event in (None, "Cancel"):	# if user closes window or clicks cancel
                break
            if event in (None, "Graph") and values[0] != "":	# if user closes window or clicks cancel
                numberOfIterations = int(values[0])
                self.handler.graphAccuracy(numberOfIterations, values[1])
            if event in (None, "Train") and values[0] != "":
                numberOfIterations = int(values[0])
                self.train(numberOfIterations, values[1])
                break


    def train(self, numberOfIterations, learningRate):
            self.handler.trainNetwork(numberOfIterations, learningRate)
            self.test()

    def test(self):
        testDirectories = {
            "English": "data/lang.test/English/",
            "German": "data/lang.test/German/",
            "Polish": "data/lang.test/Polish/"
        }
        accuracy = self.handler.classifyVectorsFromDirectories(testDirectories)
        print(accuracy)
        result = ""
        textToTest = "Enter text to test"
        while True:
            sg.theme("DarkTeal2")	
            print("init")
            layout = [  
                    [sg.Text("Accuracy: ", font=("courier", 20))] ,[sg.Text(accuracy, font=("courier", 20))],
                    [sg.Multiline(default_text=textToTest, font=("courier", 20), size=(100,20))],
                    [sg.Text("Language: ", font=("courier", 20))] ,[sg.Text(result, font=("courier", 20))],
                    [sg.Button("Run"), sg.Button("Cancel")]]
    
            window = sg.Window("Single-Layer Network", layout)
            event, values = window.read()
            if event in (None, "Cancel"):	# if user closes window or clicks cancel
                break
            if event in (None, "Run") and values[0] != "":
                textToTest = values[0]
                parser = Parser()
                result = self.handler.classifySingleVector(parser.createSimpleVector(textToTest))

        