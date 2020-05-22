from model.centroid import Centroid
from model.vector import Vector


class Cluster:
    def __init__(self, centroid: Centroid):
        self.centroid = centroid
        self.assigned_vectors = []

    def assign_vector(self, vector: Vector):
        self.assigned_vectors.append(vector)