from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

from app.retriever import load_vectorstore

def build_rag_chain():
    db = load_vectorstore()

    retriever = db.as_retriever(search_kwargs={"k": 5})

    llm = ChatOpenAI(temperature=0)

    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True,
        output_key="answer"
    )

    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        return_source_documents=True
    )

    return qa_chain


qa_chain = build_rag_chain()

def ask_question(query):
    result = qa_chain.invoke({"question": query})

    return {
        "answer": result["answer"],
        "sources": [
            {
                "source": doc.metadata.get("source"),
                "page": doc.metadata.get("page")
            }
            for doc in result["source_documents"]
        ]
    }