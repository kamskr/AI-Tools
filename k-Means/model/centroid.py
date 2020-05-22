import random


class Centroid:
    def __init__(self, dimension):
        self.centroidVector = list({random.uniform(0.0,1.0) for x in range(dimension)})


