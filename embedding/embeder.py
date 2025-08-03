from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('sentence-transformers/multi-qa-mpnet-base-cos-v1')

def encode_text(text: str) -> np.ndarray:
    embedding = model.encode(text, convert_to_tensor=False)
    return np.array(embedding, dtype="float32").reshape(1, -1)
