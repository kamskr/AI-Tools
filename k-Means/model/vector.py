import math


class Vector:
    def __init__(self, name, vector):
        self.name = name
        self.vector = vector
        self.cluster_id = int

    def calculate_distance(self, vector):
        i = 0
        sum_d = 0
        for v in self.vector:
            if i < len(vector):
                sum_d += pow(v - vector[i], 2)
            else:
                sum_d += pow(v, 2)
            i += 1

        distance = math.sqrt(sum_d)
        return distance

    def assign_to_cluster(self, cluster_id):
        self.cluster_id = cluster_id

    def set_vector(self, vector):
        self.vector = vector


