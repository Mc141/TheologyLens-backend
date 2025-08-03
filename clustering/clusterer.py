import numpy as np
import os

# Load centroids
DATA_DIR = "data"
centroids_path = os.path.join(DATA_DIR, "centroids.npy")
centroids = np.load(centroids_path)

def find_closest_clusters(query_embedding: np.ndarray, top_k: int = 5):
    """
    Returns indices of top_k closest cluster centroids to the query.
    """
    distances = np.linalg.norm(centroids - query_embedding, axis=1)
    return np.argsort(distances)[:top_k]
