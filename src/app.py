import streamlit as st

from query import rag_query

# Page configuration
st.set_page_config(
    page_title="One Piece RAG Chat",
    page_icon="☠️",
    layout="wide",
    initial_sidebar_state="collapsed"  # or "expanded"
)

# Empty sidebar
with st.sidebar:
    st.title("")

# Main title
st.title("☠️ One Piece RAG Chat")
st.caption("Ask me anything regarding the anime, One Piece")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if question := st.chat_input("Type your question..."):
    # Store and display user message
    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    with st.chat_message("user"):
        st.markdown(question)

    # Dummy chatbot response
    response = rag_query(question)

    # Store and display assistant response
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    with st.chat_message("assistant"):
        st.markdown(response)
