from service.handler import Handler
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

file_path = "data/iris.data"
number_of_clusters = 3
dimension = 4

handler = Handler(file_path, number_of_clusters, dimension)
handler.perform_clustering(40)

# vectors = []
# for vector in handler.cluster_classifier.vectors_to_classify:
#     print(vector.cluster_id)

# print(vectors)
# plt.quiver(vectors, angles='xy', scale_units='xy', scale=1)
# plt.xlim(-10, 10)
# plt.ylim(-10, 10)
# plt.show()
