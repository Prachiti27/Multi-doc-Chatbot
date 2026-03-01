import streamlit as st
import requests

BACKEND_URL = "http://localhost:8000"

st.set_page_config(page_title="Multi-Doc RAG", page_icon="💬")

st.title("Multi-Document RAG Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "uploaded" not in st.session_state:
    st.session_state.uploaded = False

with st.sidebar:
    st.header("Upload Documents")

    files = st.file_uploader(
        "Upload PDF / DOCX / TXT files",
        type=["pdf", "docx", "txt"],
        accept_multiple_files=True
    )

    if st.button("Upload Documents"):
        if not files:
            st.warning("Please select at least one document.")
        else:
            res = requests.post(
                f"{BACKEND_URL}/upload",
                files=[("files", (f.name, f.getvalue())) for f in files]
            )

            if res.status_code == 200:
                st.success("Documents uploaded successfully")
                st.session_state.uploaded = True
            else:
                st.error("Upload failed")

if not st.session_state.uploaded:
    st.info("Upload documents to start chatting.")
    st.stop()

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Ask a question about your documents...")

if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            res = requests.post(
                f"{BACKEND_URL}/chat",
                json={"question": user_input}
            )

            if res.status_code == 200:
                answer = res.json()["answer"]
            else:
                answer = "Error getting response from server."

            st.markdown(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )