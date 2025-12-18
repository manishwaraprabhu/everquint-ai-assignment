import os
import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer


class VectorStore:
    def __init__(
        self,
        model_name="all-MiniLM-L6-v2",
        vector_db_folder="vector_db"
    ):
        # Load embedding model (lightweight & fast)
        self.model = SentenceTransformer(model_name)

        self.index = None
        self.text_chunks = []
        self.vector_db_folder = vector_db_folder

    def build_index(self, chunks):
        """
        Build FAISS index from text chunks.
        Duplicate chunks are removed before embedding.
        """
        print("Preparing chunks for embedding...")

        # Extra safety: remove duplicates again
        unique_chunks = list(dict.fromkeys(chunks))

        print(f"Embedding {len(unique_chunks)} chunks...")
        embeddings = self.model.encode(
            unique_chunks,
            show_progress_bar=True
        )

        # Normalize embeddings for cosine similarity
        embeddings = np.array(embeddings).astype("float32")
        faiss.normalize_L2(embeddings)

        dimension = embeddings.shape[1]

        # Use cosine similarity (IndexFlatIP)
        self.index = faiss.IndexFlatIP(dimension)
        self.index.add(embeddings)

        self.text_chunks = unique_chunks
        print("FAISS index built successfully.")

    def save(self):
        """
        Save FAISS index and text chunks to disk.
        """
        if not os.path.exists(self.vector_db_folder):
            os.makedirs(self.vector_db_folder)

        faiss.write_index(
            self.index,
            os.path.join(self.vector_db_folder, "index.faiss")
        )

        with open(
            os.path.join(self.vector_db_folder, "chunks.pkl"),
            "wb"
        ) as f:
            pickle.dump(self.text_chunks, f)

        print("Vector DB saved.")

    def load(self):
        """
        Load FAISS index and text chunks from disk.
        """
        index_path = os.path.join(self.vector_db_folder, "index.faiss")
        chunks_path = os.path.join(self.vector_db_folder, "chunks.pkl")

        if not os.path.exists(index_path) or not os.path.exists(chunks_path):
            print("Vector DB not found.")
            return False

        self.index = faiss.read_index(index_path)

        with open(chunks_path, "rb") as f:
            self.text_chunks = pickle.load(f)

        print("Vector DB loaded.")
        return True

    def search(self, query, top_k=3):
        """
        Search for the most relevant chunks using cosine similarity.
        """
        if self.index is None:
            return []

        # Embed query
        query_embedding = self.model.encode([query])
        query_embedding = np.array(query_embedding).astype("float32")
        faiss.normalize_L2(query_embedding)

        # Search index
        scores, indices = self.index.search(query_embedding, top_k)

        results = []
        for idx in indices[0]:
            if idx < len(self.text_chunks):
                results.append(self.text_chunks[idx])

        return results