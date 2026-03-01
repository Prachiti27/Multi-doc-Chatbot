import uuid
from typing import List, Dict
from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_text(
    text: str,
    doc_id: str,
    filename: str,
    chunk_size: int = 800,
    chunk_overlap: int = 100
)->List[Dict]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    
    chunks = splitter.split_text(text)
    
    chunked_docs = []
    
    for i, chunk in enumerate(chunks):
        chunked_docs.append({
            "chunk_id": str(uuid.uuid4()),
            "doc_id": doc_id,
            "filename": filename,
            "chunk_index": i,
            "content": chunk
        })
        
    return chunked_docs