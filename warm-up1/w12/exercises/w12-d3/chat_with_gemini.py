import streamlit as st
from dotenv import load_dotenv
import os
from google import genai

load_dotenv(".credential")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Thiết kế giao diện và lưu session chat
st.title("Chat với Gemini")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display the entire conversation in the main area
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Create a sidebar for the full conversation history
with st.sidebar:
    st.subheader("Full Conversation History")
    for msg in st.session_state.messages:
        st.markdown(f"**{msg['role'].capitalize()}:** {msg['content']}")

# Gửi tin nhắn và gọi api gemini
if prompt := st.chat_input("Bạn muốn hỏi gì?"):
    st.chat_message("user").write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Format the conversation history into a single string
    conversation_history = "\n".join([
        f"{msg['role']}: {msg['content']}" for msg in st.session_state.messages
    ])

    client = genai.Client(api_key=GEMINI_API_KEY)
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=conversation_history + f"\nuser: {prompt}"
        )
        reply = response.text
        st.chat_message("assistant").write(reply)
        st.session_state.messages.append({"role": "assistant", "content": reply})
    except Exception as e:
        st.error(f"An error occurred: {e}")