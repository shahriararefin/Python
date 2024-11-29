import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min

# Sample data (replace with your dataset)
X = np.array([[12, 7, 14], [17, 8, 11], [13, 10, 12], [14, 9, 15], [15, 11, 13], [7, 5, 9]])

# Apply KMeans clustering
kmeans = KMeans(n_clusters=2, random_state=42)
kmeans.fit(X)

# Centroids of the clusters
centroids = kmeans.cluster_centers_

# 1. Intra-cluster distance (Sum of squared distances from points to their cluster center)
intra_cluster_distances = []
for i in range(kmeans.n_clusters):
    points_in_cluster = X[kmeans.labels_ == i]
    centroid = centroids[i]
    distance = np.sum(np.linalg.norm(points_in_cluster - centroid, axis=1))
    intra_cluster_distances.append(distance)

# 2. Inter-cluster distance (Distance between centroids of different clusters)
inter_cluster_distances = []
for i in range(kmeans.n_clusters):
    for j in range(i + 1, kmeans.n_clusters):
        distance = np.linalg.norm(centroids[i] - centroids[j])
        inter_cluster_distances.append(distance)

# Calculate the best cluster based on intra-cluster distance (minimize) and inter-cluster distance (maximize)
best_cluster_index = np.argmin(intra_cluster_distances)

# Display results
print("Intra-cluster distances:", intra_cluster_distances)
print("Inter-cluster distances:", inter_cluster_distances)
print(f"The best cluster is cluster {best_cluster_index + 1} based on intra-cluster distance and inter-cluster separation.")
