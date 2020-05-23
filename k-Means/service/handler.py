from model.centroid import Centroid
from service.csv_parser import CsvParser
from model.cluster import Cluster
from service.cluster_classifier import ClusterClassifier


class Handler:
    def __init__(self):
        self.training_set = []
        self.clusters = dict()
        self.cluster_classifier = ClusterClassifier

    def parse_file(self, file_path):
        csv_parser = CsvParser("./data/iris.data")
        self.training_set = csv_parser.parse_training_set()

    def create_clusters(self, number_of_clusters, dimension):
        for n in range(number_of_clusters):
            self.clusters[n] = Cluster(Centroid(dimension))

    def create_cluster_classifier(self):
        self.cluster_classifier = ClusterClassifier(self.clusters, self.training_set)


