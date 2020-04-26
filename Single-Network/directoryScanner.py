import os
from parser import Parser

class DirectoryScanner:
    def scanDirectory(self, direcotry, language):
        textFiles = []
        for file in os.listdir(direcotry):
            if file.endswith(".txt"):
                textFiles.append(os.path.join(direcotry, file))

        vectors = self.getVectorsFromDirecotry(textFiles, language)
        return vectors
        
    def getVectorsFromDirecotry(self, textFiles, language):
        vectors = []
        parser = Parser()
        for file in textFiles:
            data = parser.parseText(file)
            vectors.append(parser.createNormalizedVector(data, language))
        return vectors