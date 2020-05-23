import math

class ClusterClassifier:
    def __init__(self, clusters: dict, vectors_to_classify: []):
        self.clusters = clusters
        self.vectors_to_classify = vectors_to_classify

    def perform_iterations(self, number_of_iterations):
        for _ in range(number_of_iterations):
            self.classify_vectors()

        for cluster in self.clusters.values():
            print(len(cluster.assigned_vectors))

    def classify_vectors(self):
        for cluster in self.clusters.values():
            cluster.update_centroid()

        for vector in self.vectors_to_classify:
            distance = []

            for cluster in self.clusters.values():
                distance.append(self.calculate_distance(vector, cluster.centroid_vector))

            closest_cluster_index = distance.index(min(distance))
            print(str(vector), " distance from centroid ", min(distance))
            self.clusters.get(closest_cluster_index).assign_vector(vector)

    @staticmethod
    def calculate_distance(vector1, vector2):
        i = 0
        sum_d = 0
        for v in vector1:
            if i < len(vector2):
                sum_d += pow(v - vector2[i], 2)
            else:
                sum_d += pow(v, 2)
            i += 1

        distance = math.sqrt(sum_d)
        return distance
