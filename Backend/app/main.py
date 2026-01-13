from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.config import get_settings

from app.api.routes import router, init_store
from app.services.document_loader import DocumentLoader
from app.services.text_splitter import TextSplitter
from app.services.embedding_service import EmbeddingService
from app.services.vector_store import VectorStore

app = FastAPI(title="Government RAG Assistant")
settings = get_settings()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# build pipeline ON STARTUP 
loader = DocumentLoader(settings.DATA_DIR)
docs = loader.load_pdfs()

splitter = TextSplitter(chunk_size=settings.CHUNK_SIZE, overlap=settings.CHUNK_OVERLAP)
chunks = splitter.split(docs)

texts = [c["text"] for c in chunks]

embedder = EmbeddingService()
embeddings = embedder.embed_texts(texts)

vector_store = VectorStore(dim=embeddings.shape[1])
vector_store.add(embeddings)

init_store(vector_store, chunks)

app.include_router(router)

@app.get("/")
def root():
    return {"message": "Government RAG API is running."}

@app.get("/health")
def health():
    return {
        "app": settings.APP_NAME,
        "model": settings.LLM_MODEL,
        "top_k": settings.TOP_K,
        "status": "ok"
    }
