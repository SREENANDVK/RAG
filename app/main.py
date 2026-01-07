from fastapi import FastAPI

from app.api.routes import router, init_store
from app.services.document_loader import DocumentLoader
from app.services.text_splitter import TextSplitter
from app.services.embedding_service import EmbeddingService
from app.services.vector_store import VectorStore

app = FastAPI(title="Government RAG Assistant")

# ---- build pipeline ON STARTUP ----
loader = DocumentLoader("data/raw_docs")
docs = loader.load_pdfs()

splitter = TextSplitter(chunk_size=500, overlap=50)
chunks = splitter.split(docs)

texts = [c["text"] for c in chunks]

embedder = EmbeddingService()
embeddings = embedder.embed_texts(texts)

vector_store = VectorStore(dim=embeddings.shape[1])
vector_store.add(embeddings)

init_store(vector_store, chunks)

app.include_router(router)
