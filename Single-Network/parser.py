import math
from collections import Counter
from string import ascii_lowercase
from vector import Vector

class Parser:
    def parseText(self, myFile):
        with open(myFile, 'r') as file:
            parsedText = file.read().replace('\n','')
            return parsedText

    def createNormalizedVector(self, text, language):
        # And normalize
        vector = self.createSimpleVector(text)
        return Vector(language, vector)

    def createSimpleVector(self, text):
        counter = Counter(text)
        letterCount = []
        vector = []
        sumOfValuesSquared = 0
        for ch in ascii_lowercase:
            sumOfValuesSquared = sumOfValuesSquared + (counter[ch] * counter[ch])
            letterCount.append(counter[ch])

        vectorLength = math.sqrt(sumOfValuesSquared)

        for value in letterCount:
            vector.append(value / vectorLength)
        return vector