import streamlit as st
import requests

st.set_page_config(page_title="Multi-Doc Chatbot")

st.title("Multi-Document Chatbot")

files = st.file_uploader(
    "Upload documents",
    type=["pdf","docx","txt"],
    accept_multiple_files=True
)

if st.button("Upload") and files:
    response = requests.post(
        "http://localhost:8000/upload",
        files=[("files", (f.name, f.getvalue())) for f in files]
    )
    
    if response.status_code == 200:
        st.success("Upload Successful!")
        st.json(response.json())
    else:
        st.error("Upload failed")