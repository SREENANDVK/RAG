# Intentionally minimal.
# Add ORM models here if/when persistence is introduced.

class DocumentMeta:
    def __init__(self, source: str, page: int):
        self.source = source
        self.page = page
