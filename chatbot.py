import streamlit as st
import numpy as np

st.title("ChatBot")

if "message" not in st.session_state:
    st.session_state.message =[]

for message in st.session_state.message:
    with st.chat_message(message['role']):
        st.write(message['content'])

prompt = st.chat_input("Ask anything ........")
with st.chat_message('user'):
    st.write(prompt)
st.session_state.message.append({'role':'user','content':prompt})

with st.chat_message('assistant'):
    st.write(prompt)
st.session_state.message.append({'role':'user','content':prompt})
