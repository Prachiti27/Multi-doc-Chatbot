from langchain_groq import ChatGroq
from langchain_classic.schema import HumanMessage, SystemMessage
from backend.app.db import get_vectorstore
from backend.app.config import GROQ_API_KEY
from backend.app.prompt import build_prompt

llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name="llama-3.1-8b-instant",
    temperature=0.2
)

def retrieve_context(query: str, k: int=4)->str:
    vectordb = get_vectorstore()
    
    docs = vectordb.similarity_search(query, k=k)
    
    context = "\n\n".join(
        f"[Source: {d.metadata['filename']}]\n{d.page_content}"
        for d in docs
    )
    return context

def generate_answer(question: str) -> str:
    context = retrieve_context(question)
    prompt = build_prompt(context, question)
    response = llm.invoke(prompt)
    return response.content