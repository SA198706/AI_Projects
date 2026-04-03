from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings


def create_vectorstore(docs):
    embeddings = OpenAIEmbeddings()
    vector_db = FAISS.from_documents(docs, embeddings)
    vector_db.save_local("vectorstore")
    return vector_db

def load_vectorstore():
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    vector_db = FAISS.load_local(
    "vectorstore",
    embeddings,
    allow_dangerous_deserialization=True
)
    return vector_db