from app.services.document_loader import DocumentLoader
from app.services.text_splitter import TextSplitter
from app.services.embedding_service import EmbeddingService
from app.services.vector_store import VectorStore
import numpy as np

loader = DocumentLoader("data/raw_docs")
docs = loader.load_pdfs()

splitter = TextSplitter(chunk_size=500, overlap=50)
chunks = splitter.split(docs)

texts = [c["text"] for c in chunks]

embedder = EmbeddingService()
embeddings = embedder.embed_texts(texts)

vector_store = VectorStore(dim=embeddings.shape[1])
vector_store.add(embeddings)

query = "What is the Aadhaar Act?"
query_embedding = embedder.embed_texts([query])

scores, indices = vector_store.search(query_embedding, top_k=3)

for i in indices:
    print("----")
    print(chunks[i]["metadata"])
    print(chunks[i]["text"][:300])
