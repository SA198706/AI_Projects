from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from app.retriever import load_vectorstore

def build_rag_chain():
    db = load_vectorstore()
    retriever = db.as_retriever(search_kwargs={"k": 5})

    llm = ChatOpenAI(
        model="gpt-4",
        temperature=0
    )

    
    qa_chain = RetrievalQA.from_chain_type(
        llm=ChatOpenAI(),
        retriever=db.as_retriever(search_kwargs={"k": 5}),
        return_source_documents=True
    )

    return qa_chain


def ask_question(query: str):
    qa_chain = build_rag_chain()
    result = qa_chain(query)
    return {
        "answer": result["result"],
        "sources": [doc.metadata for doc in result["source_documents"]]
    }