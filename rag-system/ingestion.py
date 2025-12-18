import os
from PyPDF2 import PdfReader
from docx import Document


def load_pdf(file_path):
    """
    Load text content from a PDF file.
    """
    text = ""

    try:
        reader = PdfReader(file_path)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    except Exception as e:
        print(f"Error reading PDF file: {e}")

    return text.strip()


def load_docx(file_path):
    """
    Load text content from a DOCX file.
    """
    text = ""

    try:
        doc = Document(file_path)
        for para in doc.paragraphs:
            if para.text.strip():
                text += para.text.strip() + "\n"

    except Exception as e:
        print(f"Error reading DOCX file: {e}")

    return text.strip()


def chunk_text(text, chunk_size=500, overlap=50):
    """
    Split text into chunks of words with overlap.
    Duplicate and empty chunks are removed.
    """
    words = text.split()
    chunks = []
    seen_chunks = set()

    start = 0
    while start < len(words):
        end = min(start + chunk_size, len(words))
        chunk = " ".join(words[start:end]).strip()

        # Avoid empty or duplicate chunks
        if chunk and chunk not in seen_chunks:
            chunks.append(chunk)
            seen_chunks.add(chunk)

        start += chunk_size - overlap

    return chunks