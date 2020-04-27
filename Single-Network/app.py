from handler import Handler

directories = {
    "English": "data/lang/English/",
    "German": "data/lang/German/",
    "Polish": "data/lang/Polish/"
}

handler = Handler(directories)
handler.trainNetwork(50, 1)

testDirectories = {
    "English": "data/lang.test/English/",
    "German": "data/lang.test/German/",
    "Polish": "data/lang.test/Polish/"
}

handler.classifyVectorsFromDirectories(testDirectories)
# layer.train(englishVectors[0], 1)
# print(layer.classify(englishVectors[1].vector))ą