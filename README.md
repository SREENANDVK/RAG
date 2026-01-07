# Government RAG Assistant

## Overview

This project is a **Retrieval-Augmented Generation (RAG) based AI system** built to answer user questions using **official Government PDF documents** as the source of truth.

Instead of relying on a language model’s internal knowledge, the system retrieves relevant content from government documents and generates answers **strictly grounded in those documents**, reducing hallucinations and improving reliability.

This project is designed to reflect **real-world AI engineering practices**, not notebook-only experiments.

---

## Key Features

* 📄 Ingests and processes Government PDF documents
* ✂️ Chunks large documents with overlap for context preservation
* 🧠 Uses semantic embeddings for meaning-based search
* 📦 Stores vectors in FAISS for fast retrieval
* 🔍 Implements Retrieval-Augmented Generation (RAG)
* 🌐 Exposes functionality via a FastAPI backend
* 🐳 Dockerized for deployment consistency (cloud / CI-ready)

---

## Architecture

**High-level flow:**

1. Government PDFs are loaded and cleaned
2. Text is split into overlapping chunks
3. Each chunk is converted into an embedding
4. Embeddings are stored in a FAISS vector index
5. User query is embedded and semantically searched
6. Top relevant chunks are injected into the LLM prompt
7. An API-based LLM generates a grounded answer

This design keeps **retrieval and generation decoupled**, allowing easy model or provider changes.

---

## Technology Stack

* **Language:** Python
* **Backend:** FastAPI
* **Embeddings:** Sentence-Transformers (MiniLM)
* **Vector Database:** FAISS
* **LLM:** API-based (Groq – LLaMA 3.1 Instant)
* **Containerization:** Docker
* **Deployment-ready:** Yes (CI / Cloud oriented)

---

## Project Structure

```
app/
├── api/            # FastAPI routes
├── services/       # Core RAG components
│   ├── document_loader.py
│   ├── text_splitter.py
│   ├── embedding_service.py
│   ├── vector_store.py
│   └── rag_pipeline.py
├── main.py         # FastAPI app entry

data/
├── raw_docs/       # Government PDFs (ignored in Git)

Dockerfile
requirements.txt
```

---

## How RAG Is Implemented

* **Retrieval:** FAISS performs cosine similarity search over normalized embeddings
* **Augmentation:** Retrieved chunks are concatenated as context
* **Generation:** LLM is prompted to answer *only* from provided context
* **Control:** If information is missing, the model is instructed to refuse

This approach is preferred over fine-tuning for:

* Lower cost
* Faster updates
* Reduced hallucination

---

## Running Locally (Development)

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Access Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## Docker Support

The application includes a Docker configuration for consistent deployment.

```bash
docker build -t govt-rag-api .
docker run -p 8000:8000 -e GROQ_API_KEY=<key> govt-rag-api
```

> Note: Due to local RAM constraints, full image builds are intended for CI or cloud environments.

---

## Why API-Based LLMs Are Used

* Reduces local compute requirements
* Mirrors production-grade architectures
* Allows easy model switching without system redesign

---

## Future Improvements

* OCR integration for scanned PDFs
* Persistent vector storage
* Authentication & rate limiting
* Streaming responses
* Cloud deployment (AWS EC2 / ECS)

---

## Disclaimer

This project uses publicly available government documents strictly for educational and research purposes.
