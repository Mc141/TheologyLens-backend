from fastapi import APIRouter
from pydantic import BaseModel
from embedding.embeder import encode_text
from faiss_index.search_index import search_in_clusters
from clustering.clusterer import find_closest_clusters

router = APIRouter()

class Question(BaseModel):
    question: str

@router.post("/search")
async def post_question(question: Question):
    query_embedding = encode_text(question.question)
    
    # Step 1: Get closest cluster IDs
    top_clusters = find_closest_clusters(query_embedding, top_k=5)
    
    # Step 2: Search within verses of those clusters
    results = search_in_clusters(query_embedding, top_clusters, k=10)
    
    return results  # Already a list of dicts
