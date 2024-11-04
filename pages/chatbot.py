import streamlit as st 
import pandas as pd
from modules.utils.utils import pula_linha


st.title("Mecânico IA:")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["tipo_bot"]):
        st.markdown(message["conteudo"])

if prompt := st.chat_input("Digite aqui..."):
    with st.chat_message("user"):
        if prompt == "1":
            st.markdown(prompt)
        else:
            st.markdown("opa")
    st.session_state.messages.append({"tipo_bot": "user", "conteudo": prompt})
    
    response = f"echo: {prompt}"
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"tipo_bot": "assistant", "conteudo": response})
    