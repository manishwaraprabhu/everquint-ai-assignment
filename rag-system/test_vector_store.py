from ingestion import load_pdf, chunk_text
from vector_store import VectorStore

pdf_path = "EJ1172284.pdf"

text = load_pdf(pdf_path)
chunks = chunk_text(text)

vs = VectorStore()
vs.build_index(chunks)
vs.save()

# reload and test search
vs2 = VectorStore()
vs2.load()

results = vs2.search("mobile devices for english study", top_k=2)
print("\n---- Search Results ----")
for res in results:
    print(res[:200], "\n")
