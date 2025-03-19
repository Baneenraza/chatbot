import os
import google.generativeai as genai
import streamlit as st

# Configure Gemini
genai.configure(api_key="AIzaSyAicOVimMvQevQy5oKBbyZ3-4ywK7IHnk8")

# Create the model
generation_config = {
    "temperature": 0.5,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
    system_instruction="Answer everything with GenZ words and slangs. Keep it fun and casual!",
)

# Initialize session state for chat history
if "history" not in st.session_state:
    st.session_state.history = []

# Streamlit App Title
st.title("GenZ Chatbot ")
st.write("Heyyy bestie! 👋 What's up?")

# Display chat history
for message in st.session_state.history:
    with st.chat_message(message["role"]):
        st.write(message["parts"][0])

# User input
user_input = st.chat_input("Type your message here...")

if user_input:
    # Add user input to chat history
    st.session_state.history.append({"role": "user", "parts": [user_input]})

    # Display user input
    with st.chat_message("user"):
        st.write(user_input)

    # Get model response
    chat_session = model.start_chat(history=st.session_state.history)
    response = chat_session.send_message(user_input)
    model_response = response.text

    # Add model response to chat history
    st.session_state.history.append({"role": "model", "parts": [model_response]})

    # Display model response
    with st.chat_message("model", avatar="👾"):
        st.write(model_response)
