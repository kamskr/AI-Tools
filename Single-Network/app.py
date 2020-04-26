from handler import Handler

directories = {
    "English": "data/lang/English/",
    "German": "data/lang/German/",
    "Polish": "data/lang/Polish/"
}

handler = Handler(directories)
handler.trainNetwork(200, 1)

handler.classifySingleVector(handler.getSimplecVector("data/lang.test/German/2.txt"))
# layer.train(englishVectors[0], 1)
# print(layer.classify(englishVectors[1].vector))