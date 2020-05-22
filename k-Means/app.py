from model.centroid import Centroid
from service.csv_parser import CsvParser
from model.cluster import Cluster
from model.cluster_classifier import ClusterClassifier
csvParser = CsvParser("./data/iris.data")
trainingSet = csvParser.parse_training_set()
print(len(trainingSet))

centroid = Centroid(3)
cluster = Cluster(centroid)

