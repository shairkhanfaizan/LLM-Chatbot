import streamlit as st
from test_inference import get_response
import textwrap
from datetime import datetime



# Setting up streamlit page configuration
st.set_page_config(page_title="LLM chatbot", page_icon="🤖", layout="wide")
st.title("🧠 LLM Playground")

# Initialize session state for messages
if 'messages' not in st.session_state:
    st.session_state.messages = [
        {'role': "system", "content": "You are a helpful assistant."}
    ]

# sidebar Configurations
st.sidebar.title("Chat Settings")

# model selection
model_choice = st.sidebar.selectbox(
    "Select a model",
    ["mistralai/Mistral-7B-Instruct-v0.2", "gpt-3.5-turbo"],
)

# initializing clear chat button
if st.sidebar.button("Clear chat"):
    st.session_state.messages = [
        {'role': "system", "content": "You are a helpful assistant."}
    ]

# chat display
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f"😶‍🌫️ **User**: {message['content']}")
    elif message['role'] == "assistant":
        st.markdown(f"🤖 **Bot**: {message['content']}")

# user input
user_input = st.text_input("💬 Ask me anything!", key="user_input")

if user_input:
    # Append user message to session state
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    # Generate bot response
    with st.spinner("Bot is typing..."):
        try:
            reply = get_response(messages=st.session_state.messages, model=model_choice)
            # Append bot response to session state
            st.session_state.messages.append(
                {"role": "assistant", "content": reply}
            )
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Export chat conversation
if st.sidebar.button("Export chat"):
    export_text = "\n".join(
        f"{message['role'].capitalize()}: {message['content']}"
        for message in st.session_state.messages if message['role'] != "system"
    )
    st.download_button(
        "📩 Download chat",
        export_text,
        file_name=f"chat_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S %f')}.txt"
    )
    e=f"chat_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S %f')}.txt"
