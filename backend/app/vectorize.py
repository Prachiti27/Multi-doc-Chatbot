from typing import List, Dict
from langchain_classic.schema import Document
from backend.app.db import get_vectorstore

def store_chunks(chunks: List[Dict]):
    vectordb = get_vectorstore()
    documents = []
    for chunk in chunks:
        documents.append(
            Document(
                page_content=chunk["content"],
                metadata={
                    "chunk_id": chunk["chunk_id"],
                    "doc_id": chunk["doc_id"],
                    "filename": chunk["filename"],
                    "chunk_index": chunk["chunk_index"]
                }
            )
        )
        
    vectordb.add_documents(documents)
    vectordb.persist()