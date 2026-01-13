# Government RAG Assistant

## Overview

This project is a **Retrieval-Augmented Generation (RAG) based AI system** that answers user questions using **official Government PDF documents** as the source of truth.

Instead of relying on a language model’s internal knowledge, the system retrieves relevant content from government documents and generates answers **strictly grounded in those documents**, reducing hallucinations and improving reliability.

The project is structured as a **production-style backend service** with a lightweight frontend and deployment-ready configuration.

---

## Key Features

* Ingests and processes Government PDF documents
* Chunks large documents with overlap for context preservation
* Uses semantic embeddings for meaning-based search
* Stores vectors in FAISS for fast retrieval
* Implements Retrieval-Augmented Generation (RAG)
* Exposes functionality via a FastAPI backend
* Centralized, environment-driven configuration
* Graceful handling of empty or missing document indexes
* Docker-ready for CI / cloud environments

---

## Architecture

**High-level flow:**

1. Government PDFs are loaded from the data directory
2. Text is split into overlapping chunks
3. Each chunk is converted into a semantic embedding
4. Embeddings are stored in a FAISS vector index
5. User queries are embedded and semantically searched
6. Top relevant chunks are injected into the prompt
7. An API-based LLM generates a grounded answer

**Design principle:**

Retrieval and generation are **decoupled**, allowing model or provider changes without impacting the rest of the system.

### Architecture Diagram

```
┌──────────────┐
│   Frontend   │
│ (HTML / JS)  │
└──────┬───────┘
       │  HTTP POST /query
       ▼
┌──────────────┐
│   FastAPI    │
│   Backend    │
└──────┬───────┘
       │
       │ embed(query)
       ▼
┌──────────────┐
│  Embedding   │
│   Model      │
└──────┬───────┘
       │
       │ vector search
       ▼
┌──────────────┐
│   FAISS      │
│ Vector Store │
└──────┬───────┘
       │ top-k chunks
       ▼
┌──────────────┐
│  RAG Prompt  │
│  Constructor │
└──────┬───────┘
       │
       │ context + question
       ▼
┌──────────────┐
│ API-based    │
│     LLM      │
│   (Groq)     │
└──────────────┘
```

---

## Technology Stack

* **Language:** Python
* **Backend:** FastAPI
* **Embeddings:** Sentence-Transformers (MiniLM)
* **Vector Database:** FAISS
* **LLM:** API-based (Groq – LLaMA 3.1 Instant)
* **Containerization:** Docker
* **Deployment:** CI / Cloud oriented

---

## Project Structure

```
RAG Government PDF Assistant/
├── Backend/
│   ├── app/
│   │   ├── api/            # FastAPI routes
│   │   ├── services/       # Core RAG components
│   │   ├── core/           # Config & prompts
│   │   ├── db/             # Persistence placeholders
│   │   └── main.py         # FastAPI entry point
│   ├── data/
│   │   └── raw_docs/       # Government PDFs (ignored in Git)
│   ├── Dockerfile
│   ├── requirements.txt
│   └── .dockerignore
│
├── Frontend/
│   └── index.html          # Simple UI consuming the API
│
├── README.md
└── .gitignore
```

---

## How RAG Is Implemented

* **Retrieval:** FAISS performs cosine similarity search over embeddings
* **Augmentation:** Retrieved chunks are concatenated as context
* **Generation:** The LLM is prompted to answer *only* from the provided context
* **Safety:** If no documents or no relevant context exist, the API responds gracefully without crashing

This approach is preferred over fine-tuning because it offers:

* Lower cost
* Faster data updates
* Reduced hallucination risk

---

## Running Locally (Development)

```bash
cd Backend
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

The application includes Docker configuration for consistent deployment.

```bash
cd Backend
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
* Document upload & ingestion endpoint
* Authentication and rate limiting
* Streaming responses
* Cloud deployment (AWS EC2 / ECS)

---

## Disclaimer

This project uses publicly available government documents strictly for educational and research purposes.
