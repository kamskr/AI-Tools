from directoryScanner import DirectoryScanner
from singleNeuron import SingleNeuron
from singleLayer import SingleLayer

scanner = DirectoryScanner()
englishVectors = scanner.scanDirectory("data/lang/English/", "English")

englishNeuron = SingleNeuron("English")
polishNeuron = SingleNeuron("Polish")
germanNeuron = SingleNeuron("German")

layer = SingleLayer(englishNeuron, polishNeuron, germanNeuron)
layer.train(englishVectors[0].vector, "English")