from app.utils import load_pdf, split_documents
from app.retriever import create_vectorstore

def ingest(file_path: str):
    docs = load_pdf(file_path)
    chunks = split_documents(docs)
    create_vectorstore(chunks)
    print("✅ Vector DB created successfully!")

if __name__ == "__main__":
    ingest("data/irbookonlinereading.pdf")