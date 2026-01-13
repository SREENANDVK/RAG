import os
from functools import lru_cache

class Settings:
    APP_NAME = "Government RAG Assistant"

    # LLM
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    LLM_MODEL = os.getenv("LLM_MODEL", "llama-3.1-8b-instant")

    # RAG
    TOP_K = int(os.getenv("TOP_K", 3))
    CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 500))
    CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 50))

    # Paths
    DATA_DIR = os.getenv("DATA_DIR", "data/raw_docs")

@lru_cache
def get_settings():
    return Settings()
