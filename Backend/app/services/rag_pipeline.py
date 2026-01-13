import os
from groq import Groq

class RAGPipeline:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def build_prompt(self, context, question):
        return f"""
You are an assistant answering strictly from government documents.

Use ONLY the context below.
If the answer is not present, say: "Not found in the provided documents."

Context:
{context}

Question:
{question}

Answer:
""".strip()

    def generate(self, context, question):
        prompt = self.build_prompt(context, question)

        response = self.client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )

        return response.choices[0].message.content.strip()
