import numpy as np
import random


class Cluster:
    def __init__(self, dimension):
        self.centroid_vector = list({random.random() for _ in range(dimension)})
        self.assigned_vectors = []

    def assign_vector(self, vector):
        self.assigned_vectors.append(vector)

    def update_centroid(self):
        if len(self.assigned_vectors) == 0:
            return

        cluster_vectors = []
        counter = 0
        for vector in self.assigned_vectors:
            cluster_vectors.append(vector)
            counter += 1

        cluster_vector_np = np.array(cluster_vectors)
        new_centroid = np.average(cluster_vector_np, axis=0)
        self.centroid_vector = new_centroid
        self.assigned_vectors = []
