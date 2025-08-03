import os
import gdown

# Resolve the data directory relative to this file's location
current_dir = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(current_dir, "data")

FILES = {
    "bible_with_embeddings_and_clusters.csv": "https://drive.google.com/uc?id=1-h3wndQEpDdD43ruxMUMb_X7STN-TN9_",
    "centroids.npy": "https://drive.google.com/uc?id=1uhb8EVtWysVV_ps6d9WE4tc9VZ0UCHzx",
}

def ensure_data():
    os.makedirs(DATA_DIR, exist_ok=True)
    for name, url in FILES.items():
        path = os.path.join(DATA_DIR, name)
        if not os.path.exists(path):
            print(f"Downloading {name}...")
            gdown.download(url, path, quiet=False)
        else:
            print(f"{name} already exists.")
            
ensure_data()
