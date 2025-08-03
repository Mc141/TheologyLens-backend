import pandas as pd
import numpy as np
import faiss
import re
import os

# Get the absolute path of the current file
current_dir = os.path.dirname(os.path.abspath(__file__))

# Go one level up to project root
project_root = os.path.abspath(os.path.join(current_dir, ".."))

# Go into the data directory
data_dir = os.path.join(project_root, "data")

# Construct full path to the CSV file
csv_file = os.path.join(data_dir, "bible_with_embeddings_and_clusters.csv")

# Load the DataFrame
df = pd.read_csv(csv_file)



def clean_embedding(embedding_str):
    # Remove brackets and split on whitespace
    embedding_str = embedding_str.strip().replace('[', '').replace(']', '')
    embedding_values = re.split(r'\s+', embedding_str)
    return [float(v) for v in embedding_values if v]


df["embedding"] = df["Embedding"].apply(clean_embedding)
df["Cluster"] = df["Cluster"].astype(int)

embedding_matrix = np.array(df["embedding"].tolist(), dtype="float32")

# Build full FAISS index, but later we filter by cluster
d = embedding_matrix.shape[1]
full_index = faiss.IndexFlatL2(d)
full_index.add(embedding_matrix)

def build_faiss_index_for_clusters(cluster_ids: list[int]):
    filtered_df = df[df["Cluster"].isin(cluster_ids)].reset_index(drop=True)
    embeddings = np.array(filtered_df["embedding"].tolist(), dtype="float32")
    
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    
    return index, filtered_df

def search_in_clusters(query_embedding: np.ndarray, cluster_ids: list[int], k=10):
    index, verses = build_faiss_index_for_clusters(cluster_ids)
    distances, indices = index.search(query_embedding, k)
    
    # Extract relevant info + distance
    results = []
    for idx, dist in zip(indices[0], distances[0]):
        verse = verses.iloc[idx]
        results.append({
            "Reference": verse["Reference"],
            "Book Name": verse["Book Name"],
            "Chapter": int(verse["Chapter"]),
            "Verse": int(verse["Verse"]),
            "Text": verse["Text"],
            "Distance": float(dist)
        })
    return results
