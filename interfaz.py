import streamlit as st
from streamlit_chat import message as st_message
from secrets import token_bytes

if "history" not in st.session_state:
    st.session_state.history = []

st.title("Chat")

def generate_answer():
    user_message = st.session_state.input_text
    st.session_state.history.append({"message": user_message, "is_user": True, "avatar_style": "miniavs"})
    st.session_state.history.append({"message": "Juan: Hola", "is_user": False, "avatar_style": "personas"})


st.text_input("Talk to the bot", value="", key="input_text", on_change=generate_answer)

for chat in st.session_state.history:
    st_message(**chat, key=token_bytes(8))  # unpacking

