import faiss
import numpy as np

class VectorStore:
    def __init__(self, dim: int):
        self.index = faiss.IndexFlatIP(dim)

    def add(self, embeddings: np.ndarray):
        self.index.add(embeddings)

    def search(self, query_embedding: np.ndarray, top_k=5):
        scores, indices = self.index.search(query_embedding, top_k)
        return scores[0], indices[0]
