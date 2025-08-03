# TheologyLens Backend API

This is the backend API for **TheologyLens** — a tool for exploring scripture with meaning, not just words. The API serves scripture search queries and returns semantically relevant Bible verses.

---

## File Structure

```
theologylens-backend/
├── api/
│   └── routes/
│       ├── __init__.py
│       └── search.py             # Defines /search endpoint
├── clustering/
│   ├── __init__.py
│   └── clusterer.py              # Finds closest clusters using KMeans
├── embedding/
│   ├── __init__.py
│   └── embeder.py                # Generates embeddings using SentenceTransformers
├── faiss_index/
│   ├── __init__.py
│   └── search_index.py           # FAISS search logic
├── data/
│   └── (Embedding & index files downloaded into this directory)
├── main.py                       # FastAPI app entry point
├── download_data.py              # Downloads embeddings and cluster files
├── Dockerfile                    # Docker setup for API
├── requirements.txt              # Python dependencies
├── .dockerignore
├── .gitignore
└── README.md                     # You're here
```

---

## Features

- Natural language search against scripture
- Returns most contextually relevant verses
- Uses sentence embeddings + FAISS + KMeans clustering
- Clustering allows sub-1s search on full 31K verse database
- Built with FastAPI

---

## How It Works

1. A user submits a query
2. It's embedded into a high-dimensional vector
3. Top 5 closest clusters are selected using KMeans
4. FAISS performs similarity search within those clusters
5. Top 10 closest verses are returned

---

## Setup

### Option 1: Run with Docker

#### 1. Build the image

```bash
docker build -t theologylens-api .
```

#### 2. Run the container

```bash
docker run -p 8000:8000 theologylens-api
```

The API will be available at `http://localhost:8000`.

---

### Option 2: Manual Setup (Local Python)

#### 1. Clone the repository

```bash
git clone https://github.com/Mc141/TheologyLens-backend.git
cd TheologyLens-backend
```

#### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### 3. Install dependencies

```bash
pip install -r requirements.txt
```

#### 4. Download data files (embeddings, clusters, FAISS index)

```bash
python download_data.py
```

> These are hosted externally on Google Drive due to large file size.

#### 5. Run the server

```bash
fastapi dev main.py
```

API docs will be available at: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## API Endpoint

TheologyLens provides a single, optimized POST endpoint for semantic scripture search:

### `POST /search`

#### Request Body (JSON)

```json
{
  "question": "What does the Bible say about justice?"
}
```

#### Response (JSON)

Returns a list of matching verses with metadata:

```json
[
  {
    "Reference": "Amos 5:24",
    "Book Name": "Amos",
    "Chapter": 5,
    "Verse": 24,
    "Text": "But let justice roll on like rivers, and righteousness like a mighty stream.",
    "Distance": 0.6857
  }
]
```

### Description

- Uses SentenceTransformers to encode the query
- Finds top 5 clusters using cosine similarity to cluster centroids
- FAISS performs fast similarity search **within those clusters**
- Returns 10 closest verses as JSON

### Interactive Docs

Visit [http://localhost:8000/docs](http://localhost:8000/docs) to try it out.

---

## Related Repositories

### Frontend

User-facing interface to query and view results  
**Repo**: [TheologyLens Frontend](https://github.com/Mc141/TheologyLens-frontend)

### Development + Embedding Pipeline

Contains scripts used to:

- Create SentenceTransformer embeddings
- Train clustering models
- Build FAISS index

**Repo**: [TheologyLens Development](https://github.com/Mc141/TheologyLens)

---

## Tech Stack

- **FastAPI** – Async Python web framework
- **SentenceTransformers** – For semantic embeddings
- **FAISS** – For fast vector similarity search
- **KMeans (sklearn)** – To cluster 31,000+ verses for faster inference
- **Uvicorn** – ASGI server
