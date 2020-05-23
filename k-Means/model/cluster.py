from model.centroid import Centroid
from model.vector import Vector
import numpy as np


class Cluster:
    def __init__(self, centroid: Centroid):
        self.centroid = centroid
        self.assigned_vectors = []

    def assign_vector(self, vector: Vector):
        self.assigned_vectors.append(vector)

    def update_centroid(self):
        if len(self.assigned_vectors) == 0:
            return

        cluster_vectors = []
        counter = 0
        for vector_class in self.assigned_vectors:
            cluster_vectors.append(vector_class.vector)
            counter += 1

        cluster_vector_np = np.array(cluster_vectors)
        new_centroid = np.average(cluster_vector_np, axis=0)
        self.centroid.update_centroid(new_centroid)
        self.assigned_vectors = []