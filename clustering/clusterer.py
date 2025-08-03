import numpy as np
import os


# Get the absolute path of the current file
current_dir = os.path.dirname(os.path.abspath(__file__))

# Go up one level
project_root = os.path.abspath(os.path.join(current_dir, ".."))

# Into the data directory
data_dir = os.path.join(project_root, "data")

# path to centroids
centroids_path = os.path.join(data_dir, "centroids.npy")

# Load the file
centroids = np.load(centroids_path)

def find_closest_clusters(query_embedding: np.ndarray, top_k: int = 5):
    """
    Returns indices of top_k closest cluster centroids to the query.
    """
    distances = np.linalg.norm(centroids - query_embedding, axis=1)
    return np.argsort(distances)[:top_k]
