from ingestion import load_pdf, load_docx, chunk_text
import os

def test_pdf():
    sample_pdf = "EJ1172284.pdf"
    if os.path.exists(sample_pdf):
        text = load_pdf(sample_pdf)
        print("PDF loaded:", text[:200], "...")
        chunks = chunk_text(text)
        print("Number of chunks:", len(chunks))
    else:
        print("sample.pdf not found!")

def test_docx():
    sample_docx = "Project_Report_Format.docx"
    if os.path.exists(sample_docx):
        text = load_docx(sample_docx)
        print("DOCX loaded:", text[:200], "...")
        chunks = chunk_text(text)
        print("Number of chunks:", len(chunks))
    else:
        print("sample.docx not found!")

if __name__ == "__main__":
    test_pdf()
    test_docx()
