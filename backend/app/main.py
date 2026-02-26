from fastapi import FastAPI

app = FastAPI(title="Multi-Document Chat App")

@app.get("/health")
def health():
    return {"status": "ok"}