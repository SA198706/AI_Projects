from fastapi import FastAPI
from app.summarizer import ask_question

app = FastAPI()

@app.get("/")
def home():
    return {"message": "RAG Chatbot API is running 🚀"}

@app.get("/ask")
def ask(query: str):
    response = ask_question(query)
    return response