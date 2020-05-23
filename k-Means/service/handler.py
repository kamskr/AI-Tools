from service.csv_parser import CsvParser
from model.cluster import Cluster
from service.cluster_classifier import ClusterClassifier


class Handler:
    def __init__(self, file_path, number_of_clusters, dimension):
        self.training_set = []
        self.clusters = dict()
        self.cluster_classifier = ClusterClassifier
        self.initialize_handler(file_path, number_of_clusters, dimension)

    def initialize_handler(self, file_path, number_of_clusters, dimension):
        self.parse_file(file_path)
        self.create_clusters(number_of_clusters, dimension)
        self.create_cluster_classifier()

    def parse_file(self, file_path):
        csv_parser = CsvParser(file_path)
        self.training_set = csv_parser.parse_training_set()

    def create_clusters(self, number_of_clusters, dimension):
        for n in range(number_of_clusters):
            self.clusters[n] = Cluster(dimension)

    def create_cluster_classifier(self):
        self.cluster_classifier = ClusterClassifier(self.clusters, self.training_set)

    def perform_clustering(self, number_of_iterations):
        self.cluster_classifier.perform_iterations(number_of_iterations)
