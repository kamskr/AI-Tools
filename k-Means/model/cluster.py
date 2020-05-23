from model.centroid import Centroid
from model.vector import Vector
import numpy as np
import statistics


class Cluster:
    def __init__(self, centroid: Centroid):
        self.centroid = centroid
        self.assigned_vectors = []

    def assign_vector(self, vector: Vector):
        self.assigned_vectors.append(vector)

    def update_centroid(self):
        cluster_vectors = np.array()
        for vector_class in self.assigned_vectors:
            np.append(cluster_vectors, vector_class.vector, axis=None)

        new_centroid = np.average(cluster_vectors, axis=0)
        print(new_centroid)