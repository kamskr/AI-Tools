import math


class Vector:
    def __init__(self, name, vector):
        self.name = name
        self.vector = vector

    def calculate_distance(self, vector):
        i = 0
        sum = 0
        for v in self.vector:  
            if i < len(vector):
                sum += pow(v-vector[i], 2)
            else:
                sum += pow(v, 2)
            i += 1

        distance = math.sqrt(sum)
        return distance, self.name