from model.cluster import Cluster
from model.vector import Vector


class ClusterClassifier:
    def __init__(self, clusters: dict, vectors_to_classify: [Vector]):
        self.clusters = clusters
        self.vectors_to_classify = vectors_to_classify

    def perform_iterations(self, number_of_iterations):
        for _ in range(number_of_iterations):
            self.classify_vectors()

    def classify_vectors(self):
        for vector in self.vectors_to_classify:
            distance = []
            for cluster in self.clusters.values():
                distance.append(vector.calculate_distance(cluster.centroid.centroidVector))

            closest_cluster_index = distance.index(min(distance))
            self.clusters.get(closest_cluster_index).assign_vector(vector)
            vector.assign_to_cluster(closest_cluster_index)

        for cluster in self.clusters.values():
            cluster.update_centroid()
