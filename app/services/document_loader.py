from pathlib import Path
import pdfplumber

class DocumentLoader:
    def __init__(self, data_dir: str):
        self.data_dir = Path(data_dir)

    def load_pdfs(self):
        documents = []

        for pdf_path in self.data_dir.glob("*.pdf"):
            with pdfplumber.open(pdf_path) as pdf:
                for page_num, page in enumerate(pdf.pages, start=1):
                    text = page.extract_text()

                    if text and text.strip():
                        documents.append({
                            "text": text.strip(),
                            "metadata": {
                                "source": pdf_path.name,
                                "page": page_num
                            }
                        })

        return documents