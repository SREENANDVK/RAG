from fastapi import APIRouter
from pydantic import BaseModel

from app.services.embedding_service import EmbeddingService
from app.services.vector_store import VectorStore
from app.services.rag_pipeline import RAGPipeline

router = APIRouter()

# ---- request/response schemas ----
class QueryRequest(BaseModel):
    question: str

class QueryResponse(BaseModel):
    answer: str

# ---- initialize shared services (simple version) ----
embedder = EmbeddingService()
rag = RAGPipeline()

# NOTE: vector_store & chunks will be injected from main app
vector_store = None
chunks = None

def init_store(store, chunk_data):
    global vector_store, chunks
    vector_store = store
    chunks = chunk_data

@router.post("/query", response_model=QueryResponse)
def query_rag(req: QueryRequest):
    query_embedding = embedder.embed_texts([req.question])
    _, indices = vector_store.search(query_embedding, top_k=3)

    context = "\n\n".join([chunks[i]["text"] for i in indices])
    answer = rag.generate(context, req.question)

    return {"answer": answer}
