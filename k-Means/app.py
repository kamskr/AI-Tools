from model.centroid import Centroid
from service.csv_parser import CsvParser
from model.cluster import Cluster
from service.cluster_classifier import ClusterClassifier
import numpy as np


# trainingSet =
for vector in trainingSet:
    print(str(vector.vector), ' ', vector.name)


c = ClusterClassifier(clist, trainingSet)

for cl in c.clusters.values():
    print(cl)

data = np.array([[2, 2, 4], [5, 6, 7]])
print(np.average(data, axis=0)[0])


