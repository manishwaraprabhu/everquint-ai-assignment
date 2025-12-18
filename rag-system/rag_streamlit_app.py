import streamlit as st
from rag_chain import RAGSystem
import tempfile
import os

# PAGE CONFIG
st.set_page_config(
    page_title="RAG Document Search & Summarization",
    layout="centered"
)

# TITLE
st.title("📄 RAG Document Summarization System")
st.markdown(
    """
    Upload a document and get a **concise, context-aware summary** using
    a Retrieval-Augmented Generation (RAG) pipeline.
    """
)

st.divider()

# INITIALIZE RAG SYSTEM
if "rag_bot" not in st.session_state:
    st.session_state.rag_bot = RAGSystem(model_name="phi3:mini")

bot = st.session_state.rag_bot

# DOCUMENT UPLOAD
st.subheader("📂 Document Upload")

uploaded_file = st.file_uploader(
    "Upload a document (PDF or DOCX)",
    type=["pdf", "docx"]
)

if uploaded_file:
    file_suffix = os.path.splitext(uploaded_file.name)[1]
    with tempfile.NamedTemporaryFile(delete=False, suffix=file_suffix) as tmp_file:
        tmp_file.write(uploaded_file.read())
        temp_path = tmp_file.name

    with st.spinner("Ingesting document and building vector index..."):
        bot.ingest_document(temp_path)

    st.success("Document successfully ingested and indexed.")
    os.remove(temp_path)

st.divider()

# SEARCH QUERY
st.subheader("📝 Enter Your Question")

query = st.text_input(
    "Type your question here",
    placeholder="e.g., What is the main objective of the document?"
)

search_clicked = st.button("🔍 Get Summary / Answer")

# OUTPUT SECTION
if search_clicked:
    if not query.strip():
        st.warning("Please enter a valid question.")
    else:
        with st.spinner("Generating concise answer from the document..."):
            # Fixed top_k internally
            summary = bot.query(query, top_k=5)

        st.subheader("🧾 Answer / Summary")
        st.write(summary)

else:
    st.info("Upload a document, type a question, and click **Get Summary / Answer**.")