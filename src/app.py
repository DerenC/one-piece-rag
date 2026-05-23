import streamlit as st

from query import rag_query

# Page configuration
st.set_page_config(
    page_title="OnePieceGPT",
    page_icon="☠️",
    layout="wide",
    initial_sidebar_state="collapsed"  # or "expanded"
)

# Empty sidebar
with st.sidebar:
    st.title("")

# Main title
st.title("☠️ OnePieceGPT")
st.caption("Ask me anything regarding the anime, One Piece")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

        if message["role"] == "assistant" and message.get("sources"):
            with st.expander("Sources"):
                for i, source in enumerate(message["sources"]):
                    st.markdown(f"**Source {i+1}:** {source}")

# Chat input
if question := st.chat_input("Type your question..."):
    # Store and display user message
    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    with st.chat_message("user"):
        st.markdown(question)

    response, sources = rag_query(question)

    # Store and display assistant response
    st.session_state.messages.append(
        {"role": "assistant", "content": response, "sources": sources}
    )

    with st.chat_message("assistant"):
        st.markdown(response)

        with st.expander("Sources"):
            for i, source in enumerate(sources):
                st.markdown(f"**Source {i+1}:** {source}")
