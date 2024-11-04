import streamlit as st 
from datetime import datetime,timedelta
import requests
import json
import time
import pandas as pd
from modules.database.usuario import visualizar_user, visualizar_cliente, atualiza_user,atualiza_cliente

lista_sexo = ["M", "F"]

@st.dialog("Atualizar infos: ")
def atualizar_user(id:int):
    user = visualizar_user(id)
    cliente = visualizar_cliente(id)
    nome = st.text_input("Nome: ", value=user["nome"])
    sobrenome = st.text_input("Sobrenome:" ,value=user["sobrenome"])
    email = st.text_input("E-mail: ", value=user["email"])
    senha = st.text_input("Senha: " ,value=user["senhaHashed"], placeholder="")
    telefone = st.text_input("Telefone: ", value=user["telefoneCelular"])
    cpf = st.text_input("CPF: ", value=cliente["CPFCliente"])
    cnh = st.text_input("CNH: ", value=cliente["numeroCNH"])
    sexo = st.selectbox("Sexo", lista_sexo, index=lista_sexo.index(cliente["sexo"])) 
    min_date = datetime.today() - timedelta(days=100 * 365)
    data_obj = datetime.strptime(cliente["dataNascimento"], "%Y-%m-%d")
    data_de_nasc = st.date_input("Data de nascimento", data_obj, min_value=min_date) 
    data_formatada = data_de_nasc.strftime("%Y-%m-%d")
    if st.button("Atualizar"):
        user_new ={
        "email": email,
        "nome": nome,
        "senhaHashed": senha,
        "sobrenome": sobrenome,
        "telefoneCelular": telefone,
        "tipoUsuario": "cliente",
        }
        cliente_new = {
            "CPFCliente": cpf,
            "dataNascimento": data_formatada,
            "numeroCNH": cnh,
            "sexo": sexo
            }
       
        try:
            atualiza_user(id,user_new)
            atualiza_cliente(id,cliente_new)
            st.success("usuario atualizado com sucesso")
            time.sleep(5)
            st.rerun()
        except requests.exceptions.HTTPError as err:
            if err.response.status_code == 422:
                st.error("Erro de validação: os dados enviados não estão corretos.")
            else:
                st.error(f"Erro ao criar a tarefa: {err}")
            
            st.write("Resposta da API:", err.response.text)

        except json.JSONDecodeError:
            st.error("Erro ao processar a resposta da API. Resposta inválida.")

        except Exception as e:
            st.error(f"Ocorreu um erro inesperado: {e}")
    

@st.dialog("Infos User")
def infos_user(id:int):
    user = visualizar_user(id)
    cliente = visualizar_cliente(id)
    st.write(f"Nome: {user["nome"]}")
    st.write(f"Sobrenome: {user["sobrenome"]}")
    st.write(f"email: {user["email"]}")
    st.write(f"Telefone: {user["telefoneCelular"]}")
    st.write(f"CPF: {cliente["CPFCliente"]}")
    st.write(f"Sexo: {cliente["sexo"]}")
    st.write(f"CNH: {cliente["numeroCNH"]}")
    data_formatada = cliente["dataNascimento"].replace("-", "/")
    st.write(f"Data de nascimento: {data_formatada}")
