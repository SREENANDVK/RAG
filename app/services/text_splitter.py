class TextSplitter:
    def __init__(self, chunk_size=500, overlap=50):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def split(self, documents):
        chunks = []

        for doc in documents:
            text = doc["text"]
            metadata = doc["metadata"]

            start = 0
            text_length = len(text)

            while start < text_length:
                end = start + self.chunk_size
                chunk_text = text[start:end]

                if chunk_text.strip():
                    chunks.append({
                        "text": chunk_text,
                        "metadata": metadata
                    })

                start = end - self.overlap

        return chunks