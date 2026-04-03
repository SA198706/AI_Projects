import streamlit as st
import requests

st.set_page_config(page_title="RAG Chatbot", page_icon="🤖")

st.title("🤖 RAG-Based Chatbot")
st.write("Ask questions from your document")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
query = st.chat_input("Ask something...")

if query:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.write(query)

    # Call FastAPI backend
    response = requests.get(
        "http://127.0.0.1:8001/ask",
        params={"query": query}
    )

    if response.status_code == 200:
        answer = response.json()["answer"]

        # Show bot response
        st.session_state.messages.append({"role": "assistant", "content": answer})
        with st.chat_message("assistant"):
            st.write(answer)
    else:
        st.error("Error connecting to backend")