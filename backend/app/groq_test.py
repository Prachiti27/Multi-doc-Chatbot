from langchain_groq import ChatGroq
from config import GROQ_API_KEY

llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name="llama-3.1-8b-instant"
)

response = llm.invoke("Say hello in one sentence.")
print(response.content)