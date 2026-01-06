from app.services.document_loader import DocumentLoader
from app.services.text_splitter import TextSplitter
from app.services.embedding_service import EmbeddingService

loader = DocumentLoader("data/raw_docs")
docs = loader.load_pdfs()

splitter = TextSplitter(chunk_size=500, overlap=50)
chunks = splitter.split(docs)

texts = [c["text"] for c in chunks]

embedder = EmbeddingService()
embeddings = embedder.embed_texts(texts)

print(f"Total chunks: {len(chunks)}")
print(f"Embedding shape: {embeddings.shape}")
