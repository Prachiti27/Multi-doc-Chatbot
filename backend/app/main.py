from fastapi import FastAPI, UploadFile, File
from pathlib import Path
import uuid
from backend.app.ingest import extract_text, UPLOAD_DIR

app = FastAPI(title="Multi-Document Chat App")

@app.post("/upload")
async def upload_documents(files: list[UploadFile] = File(...)):
    documents = []
    
    for file in files:
        doc_id = str(uuid.uuid4())
        file_path = UPLOAD_DIR/f"{doc_id}_{file.filename}"
        with open(file_path, "wb") as f:
            f.write(await file.read())
            
        text = extract_text(file_path)
        
        documents.append({
            "doc_id": doc_id,
            "filename": file.filename,
            "text_length": len(text)
        })
        
    return {
        "message": "Documents uploaded successfully",
        "documents": documents
    }

@app.get("/health")
def health():
    return {"status": "ok"}