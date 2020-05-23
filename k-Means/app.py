from service.handler import Handler


file_path = "./data/iris.data"
number_of_clusters = 3
dimension = 4

handler = Handler(file_path, number_of_clusters, dimension)
handler.perform_clustering(2)

for vector in handler.cluster_classifier.clusters.values():
    print(vector.centroid.centroidVector)
# data = np.array([[2, 2, 4], [5, 6, 7]])
# print(np.average(data, axis=0)[0])


