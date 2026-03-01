SYSTEM_PROMPT = """
You are a helpful assistant.
Answer the question ONLY using the provided context.
If the answer is not present in the context, say:
"I could not find this information in the provided documents."
"""

def build_prompt(context: str, question: str) -> str:
    return f"""
{SYSTEM_PROMPT}

Context:
{context}

Question:
{question}
"""