# Document Search and Summarization Using Large Language Models (LLM)

## Project Overview

This project implements a **Retrieval-Augmented Generation (RAG) system** that allows users to **search, retrieve, and summarize documents** efficiently using a Large Language Model (LLM). The system is designed to work with PDFs and DOCX files and provides concise, context-aware summaries for user queries.

The goal is to **combine document search capabilities with LLM-powered summarization**, enabling fast and accurate information retrieval from large text corpora.

---

## Features

- **Document Ingestion:** Upload PDF or DOCX files and automatically extract text.
- **Text Chunking:** Documents are split into chunks to enhance search and summarization efficiency.
- **Vector Embeddings:** Text chunks are embedded using a lightweight transformer model and stored in a FAISS vector database for similarity search.
- **RAG Pipeline:** Retrieves the most relevant chunks for a query and generates a concise answer using an LLM.
- **Streamlit UI:** User-friendly interface to upload documents, enter queries, and get summaries.
- **Contextual Accuracy:** Answers strictly based on the provided document context; avoids speculation.
- **Optional Contextual Memory & Caching:** (Advanced) Support for remembering previous queries to reduce latency.

---

## System Architecture

1. **Data Ingestion**
   - Supports PDF and DOCX files.
   - Extracted text is preprocessed and split into overlapping chunks.
   
2. **Vector Store**
   - Uses **Sentence Transformers** to embed chunks.
   - Stores embeddings in **FAISS** for fast similarity searches.
   - Duplicate chunks are removed for efficiency.

3. **Query Processing**
   - User enters a question.
   - Top K relevant chunks are retrieved using cosine similarity.
   - Lightweight reranking prioritizes chunks with overlapping keywords.
   - Context is provided to the LLM for generating concise answers.

4. **Answer Generation**
   - LLM (e.g., Ollama `phi3:mini`) generates a summary or answer based only on retrieved chunks.
   - Output length and relevance are controlled.

---

## Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/rag-document-summarization.git
cd rag-document-summarization
````

### 2. Setup Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate.bat  # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

### 1. Test Document Ingestion

```bash
python test_ingestion.py
```

* Checks PDF and DOCX ingestion.
* Splits text into chunks.
* Prints the number of chunks created.

### 2. Test Vector Store

```bash
python test_vector_store.py
```

* Builds a FAISS index of document chunks.
* Tests similarity search with sample queries.

### 3. Run RAG CLI

```bash
python rag_chain.py
```

* Command-line interface to ask questions based on ingested documents.
* Type `exit` to quit.

### 4. Run Streamlit UI

```bash
streamlit run rag_streamlit_app.py
```

* Upload a document.
* Enter your query.
* Get a concise summary or answer from the document.

---

## Example Queries & Outputs

### Question

> What is the main purpose of this research paper?

### Answer

> The primary goal of this study was to explore how smartphones, tablets, and computers facilitate English learning among students with varying proficiency levels at a private university in Tehran. The investigation aimed to understand the factors influencing their engagement with mobile-assisted language learning (MALL) tools during free periods or breaks...

### Negative/Absence Check

> Question: Does the study suggest that all students benefit equally from mobile device usage for language learning?
> Answer: The document does not provide this information.

### Specific Detail

> Question: Which mobile apps were mentioned for English learning?
> Answer: WhatsApp Messenger, Fiszkoteka app, vocabulary-building apps, Six Minutes English podcast, and scanned PDF materials.

---

## Code Structure

```
rag-system/
│
├── ingestion.py          # Document loading & chunking
├── vector_store.py       # FAISS vector store management
├── rag_chain.py          # RAG system class & query pipeline
├── rag_streamlit_app.py  # Streamlit UI for document search & summarization
├── test_ingestion.py     # Test scripts for ingestion
└── test_vector_store.py  # Test scripts for vector store & search
```

---

## Evaluation Criteria

* **Functionality:** Efficient document search and summarization.
* **Accuracy:** Relevance of retrieved documents and quality of summaries.
* **Efficiency:** Fast query response with large corpora.
* **Scalability:** Works for multiple and large documents.
* **Code Quality:** Modular, clean, and well-documented.
* **Report Quality:** Clear explanation of methodology, preprocessing, and evaluation.

---

## Advanced Suggestions

* Fine-tune the LLM on domain-specific corpus for better performance.
* Implement caching to reduce response time for repeated queries.
* Use auto-suggestion and pagination in Streamlit UI for improved user experience.
* Integrate larger LLMs for more complex queries if computational resources allow.

---

## References

* [FAISS: A library for efficient similarity search](https://github.com/facebookresearch/faiss)
* [Sentence Transformers](https://www.sbert.net/)
* [Streamlit Documentation](https://docs.streamlit.io/)
* [Ollama API](https://ollama.com/docs)