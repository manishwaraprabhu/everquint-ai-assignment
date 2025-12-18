from vector_store import VectorStore
from ingestion import load_pdf, load_docx, chunk_text
import ollama
import os


class RAGSystem:
    """
    Optimized Retrieval-Augmented Generation system.
    Fast and accurate for local execution using Ollama.
    """

    def __init__(self, model_name="phi3:mini"):
        self.model_name = model_name

        # Initialize vector store
        self.vs = VectorStore()

        # Try loading existing vector DB
        loaded = self.vs.load()
        if loaded:
            print("Vector database loaded successfully.")
        else:
            print("No existing vector database found. Please ingest a document.")

    # DOCUMENT INGESTION
    def ingest_document(self, file_path: str):
        """
        Ingest a PDF or DOCX document, split into chunks,
        embed them, and store in FAISS vector database.
        """

        if not os.path.exists(file_path):
            raise FileNotFoundError("Uploaded document not found.")

        # Detect file type
        if file_path.lower().endswith(".pdf"):
            text = load_pdf(file_path)
        elif file_path.lower().endswith(".docx"):
            text = load_docx(file_path)
        else:
            raise ValueError("Unsupported file type. Only PDF and DOCX are allowed.")

        if not text.strip():
            raise ValueError("No text could be extracted from the document.")

        # Chunk text
        chunks = chunk_text(text)

        if not chunks:
            raise ValueError("Document could not be chunked.")

        # Build and save vector index
        self.vs.build_index(chunks)
        self.vs.save()

        return True

    # INTERNAL UTILITIES
    def _rerank_chunks(self, question, chunks):
        """
        Lightweight reranking based on keyword overlap.
        Fast and suitable for CPU-only systems.
        """
        q_words = set(question.lower().split())
        scored_chunks = []

        for chunk in chunks:
            c_words = set(chunk.lower().split())
            score = len(q_words.intersection(c_words))
            scored_chunks.append((score, chunk))

        scored_chunks.sort(reverse=True, key=lambda x: x[0])
        return [chunk for _, chunk in scored_chunks]

    def _trim_chunk(self, text, max_chars=800):
        """
        Limit chunk size to reduce LLM latency while keeping context.
        """
        return text[:max_chars].strip()

    # QUERY PIPELINE
    def query(self, user_query, top_k=5, max_words=120):
        # Step 1: Retrieve relevant chunks
        retrieved_chunks = self.vs.search(user_query, top_k=top_k)
        if not retrieved_chunks:
            return "The document does not provide this information."

        # Step 2: Rerank retrieved chunks
        reranked = self._rerank_chunks(user_query, retrieved_chunks)

        # Step 3: Select and trim top 3 chunks
        selected_chunks = [self._trim_chunk(chunk) for chunk in reranked[:3]]
        context = "\n\n".join(selected_chunks)

        # Step 4: Controlled prompt
        prompt = f"""
You are answering a question using only the provided context.

Rules:
- Use only information from the context
- Be concise and directly answer the question
- Do NOT speculate or infer beyond the context
- Do NOT cite external authors, studies, or references
- If the answer is not in the context, say:
  "The document does not provide this information."

Context:
{context}

Question:
{user_query}

Answer in no more than {max_words} words.
"""

        try:
            response = ollama.chat(
                model=self.model_name,
                messages=[{"role": "user", "content": prompt}]
            )
            return response["message"]["content"].strip()

        except Exception as e:
            return f"Error generating response: {e}"


# CLI TEST
if __name__ == "__main__":
    bot = RAGSystem()
    print("=== RAG Question Answering ===")

    while True:
        question = input("\nAsk a question (or type exit): ")
        if question.lower() == "exit":
            break

        answer = bot.query(question)
        print("\nAnswer:\n", answer)
