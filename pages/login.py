import streamlit as st 
import time
import json
from modules.utils.utils import pula_linha
from modules.database.usuario import visualizar, apagar_user, visualizar_user
from modules.dialog.dialogs_user import infos_user, atualizar_user

lista_users = visualizar()
user = visualizar_user(st.session_state.id)

st.title("login:")
with st.container(height=200):
    email = st.text_input("E-mail: ", placeholder="Digite seu e-mail")
    senha = st.text_input("Senha: ", placeholder="Crie uma senha", type="password")
    
if st.button("Login"):
    for user in lista_users:
        if user["email"] == email and user["senhaHashed"] == senha:
            st.session_state.login = True
            st.session_state.id = user["idUser"]
        else:
            st.session_state.login = False
            st.session_state.id = None
    if st.session_state.login:
        st.session_state.message_login = "Usuario logado!"
    else:
        st.error("Usuario não encontrado!")

if st.session_state.login:
        st.success(st.session_state.message_login)
        if st.button("Info Login"):
            infos_user(st.session_state.id)
        if st.button("alterar infos"):
            atualizar_user(st.session_state.id)
        if st.button("apagar conta"):
            apagar_user(st.session_state.id)
            st.success("User deletado com sucesso.")
            time.sleep(1)
            st.session_state.login = False
            st.rerun()
            
        json_data = json.dumps(user, indent=4)

        st.download_button(
            label="Baixar JSON",
            data=json_data,
            file_name="dados_user.json",
            mime="application/json"
        )
        

