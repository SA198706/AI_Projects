# RAG-Based Chatbot using LangChain, FAISS & FastAPI

## Overview

This project implements a Retrieval-Augmented Generation (RAG) chatbot that allows users to query information from PDF documents. It combines semantic search (FAISS) with an LLM to generate accurate, context-aware responses. The chatbot supports multi-turn conversations using memory.


## Features

PDF document ingestion
Text chunking
Embedding generation
Vector storage using FAISS
Semantic search (top-k retrieval)
LLM-based response generation
Conversational memory (multi-turn chat)
FastAPI backend
Streamlit UI
Source attribution

Architecture
User → Streamlit UI → FastAPI → Retriever (FAISS) → LLM → Response

## Project Structure

rag-chatbot/

├── app/
│ ├── main.py
│ ├── utils.py
│ ├── retriever.py
│ ├── summarizer.py
│
├── data/
│ └── irbookonlinereading.pdf
│
├── vectorstore/
├── chat_ui.py
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
6. Pass context + query to LLM
6. LLM generates answer using retrieved context

## Conversational Memory

Supports follow-up questions
Maintains chat history
Enables context-aware responses


## Example Query

Input:
User: What is Information Retrieval?
User: What are its applications?



## Tech Stack

* Python
* LangChain
* OpenAI (GPT-3.5 Turbo)
* FAISS
* FastAPI
* PyPDF
* Streamlit


## Future Improvements

* Add Reranking
* Multi-document support
* UI enhancements
* Use open-source LLMs
* Deploy on cloud platforms


## Author

Saranya Alagarsamy


## Note

This project demonstrates a complete end-to-end RAG pipeline including ingestion, vector storage, retrieval with conversational memory and response generation for building context-aware AI applications.
