import streamlit as st
from client import generate_completion

st.title("GPT4All DeepSeek Chatbot")

# Store the conversation history in Streamlit's session state.
# This prevents the app from losing the chat history on every rerun.
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages.
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle user input.
user_prompt = st.chat_input("Enter your message...")
if user_prompt:
    # Display user message in the chat message container.
    with st.chat_message("user"):
        st.markdown(user_prompt)
    # Add user message to chat history.
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    
    # Generate and display assistant response.
    with st.chat_message("assistant"):
        with st.spinner("Generating response..."):
            response = generate_completion(user_prompt)
            st.markdown(response)
    # Add assistant response to chat history.
    st.session_state.messages.append({"role": "assistant", "content": response})