from fastapi import FastAPI, UploadFile, File
from pathlib import Path
import uuid
from backend.app.ingest import extract_text, UPLOAD_DIR
from backend.app.chunker import chunk_text
from backend.app.vectorize import store_chunks

app = FastAPI(title="Multi-Document Chat App")

@app.post("/upload")
async def upload_documents(files: list[UploadFile] = File(...)):
    all_chunks = []
    
    for file in files:
        doc_id = str(uuid.uuid4())
        file_path = UPLOAD_DIR/f"{doc_id}_{file.filename}"
        
        with open(file_path, "wb") as f:
            f.write(await file.read())
            
        text = extract_text(file_path)
        chunks = chunk_text(
            text=text,
            doc_id=doc_id,
            filename=file.filename
        )
        
        all_chunks.extend(chunks)
        
        store_chunks(all_chunks)
        
        return {
            "message": "Docs embedded and stored",
            "documents": len(files),
            "total_chunks": len(all_chunks)
        }

@app.get("/health")
def health():
    return {"status": "ok"}