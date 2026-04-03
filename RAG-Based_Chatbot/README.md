# RAG-Based Chatbot using LangChain, FAISS & FastAPI

## Overview

This project implements a Retrieval-Augmented Generation (RAG) chatbot that allows users to query information from a PDF document. The system retrieves relevant content from the document and generates accurate, context-aware responses using an LLM.


## Features

* PDF document ingestion
* Text chunking for efficient retrieval
* Embedding generation using OpenAI
* Vector database using FAISS
* Semantic search (top-k retrieval)
* Context-aware response generation
* FastAPI backend for querying
* Source-based answers (page references)


## Project Structure

rag-chatbot/

│
├── app/
│   ├── main.py
│   ├── utils.py
│   ├── retriever.py
│   ├── summarizer.py
│
├── data/
│   └── irbookonlinereading.pdf
│
├── vectorstore/
│
├── ingest.py
├── .env
└── README.md


## Setup Instructions

1. Create Environment
   conda create -n rag_env python=3.10 -y
   conda activate rag_env

2. Install Dependencies
   pip install langchain==0.1.17 openai==0.28.1 faiss-cpu fastapi uvicorn python-dotenv pypdf tiktoken

3. Set API Key
   Create a .env file and add:
   OPENAI_API_KEY=your_api_key_here

4. Run Ingestion
   python ingest.py

5. Start API
   uvicorn app.main:app --reload

6. Test the Chatbot
   Open in browser:
   http://127.0.0.1:8000/ask?query=Define information retrieval


## How It Works

1. PDF is loaded and split into chunks
2. Chunks are converted into embeddings
3. Stored in FAISS vector database
4. Query is converted into embedding
5. Top-k similar chunks are retrieved
6. LLM generates answer using retrieved context


## Example Query

Input:
Define information retrieval?

Output:
{
"answer": "Information retrieval is the process...",
"sources": [
{"page": 201},
{"page": 206}
]
}


## Tech Stack

* Python
* LangChain
* OpenAI API
* FAISS
* FastAPI
* PyPDF


## Future Improvements

* Add chat UI (Streamlit or React)
* Add conversational memory
* Improve retrieval using reranking
* Use open-source LLMs
* Deploy on cloud platforms


## Author

Saranya Alagarsamy


## Note

This project demonstrates a complete end-to-end RAG pipeline including ingestion, vector storage, retrieval, and response generation.
