import os
import requests

DATA_DIR = "data"
FILES = {
    "bible_with_embeddings_and_clusters.csv": "https://drive.google.com/uc?export=download&id=1-h3wndQEpDdD43ruxMUMb_X7STN-TN9_",
    "centroids.npy": "https://drive.google.com/uc?export=download&id=1uhb8EVtWysVV_ps6d9WE4tc9VZ0UCHzx",
}

def download_file(name, url):
    path = os.path.join(DATA_DIR, name)
    if os.path.exists(path):
        print(f"[✓] {name} already exists.")
        return

    print(f"[↓] Downloading {name}...")
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        print(f"[✓] Saved to {path}")
    else:
        raise Exception(f"Failed to download {name}: {response.status_code} - {response.text}")

def ensure_data():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    for name, url in FILES.items():
        download_file(name, url)

if __name__ == "__main__":
    ensure_data()
