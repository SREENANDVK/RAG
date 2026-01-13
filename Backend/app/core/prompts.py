SYSTEM_PROMPT = """You are a factual assistant.
Answer ONLY using the provided context.
If the answer is not present in the context, say:
'I don’t have enough information from the documents.'"""

def build_prompt(context: str, question: str) -> str:
    return f"""
{SYSTEM_PROMPT}

Context:
{context}

Question:
{question}

Answer:
"""
