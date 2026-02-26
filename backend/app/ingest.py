import uuid
from pathlib import Path
from typing import List
from pypdf import PdfReader
from docx import Document

UPLOAD_DIR = Path("data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

def load_pdf(path: Path) -> str:
    reader = PdfReader(path)
    text = []
    for page in reader.pages:
        if page.extract_text():
            text.append(page.extract_text())
    return "\n".join(text)

def load_docx(path: Path) -> str:
    doc = Document(path)
    return "\n".join([p.text for p in doc.paragraphs])

def load_txt(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")

def extract_text(file_path: Path) -> str:
    suffix = file_path.suffix.lower()
    
    if suffix == ".pdf":
        return load_pdf(file_path)
    elif suffix == ".docx":
        return load_docx(file_path)
    elif suffix == ".txt":
        return load_txt(file_path)
    else:
        raise ValueError("Unsupported file type")