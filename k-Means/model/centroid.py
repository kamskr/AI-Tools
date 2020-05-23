import random


class Centroid:
    def __init__(self, dimension):
        self.centroidVector = list({random.uniform(-5,5) for x in range(dimension)})

    def update_centroid(self, vector):
        self.centroidVector = vector

