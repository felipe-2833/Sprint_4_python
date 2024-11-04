import streamlit as st 
from datetime import datetime, timedelta
import time
import json
import requests
from modules.utils.utils import pula_linha
from modules.database.usuario import criar_cliente

st.title("Cadastro:")
with st.container(height=400):
    nome = st.text_input("Nome: ", placeholder="Digite seu nome")
    sobrenome = st.text_input("Sobrenome: ", placeholder="Digite seu sobrenome")
    email = st.text_input("E-mail: ", placeholder="Digite seu e-mail")
    senha = st.text_input("Senha: ", placeholder="Crie uma senha", type="password")
    telefone = st.text_input("Telefone: ", placeholder="Digite seu telefone")
    cpf = st.text_input("CPF: ", placeholder="Digite seu cpf")
    cnh = st.text_input("CNH: ", placeholder="Digite o numero da sua CNH")
    sexo = st.selectbox("Sexo", ["M", "F"], index= None, placeholder="Escolha seu sexo") 
    min_date = datetime.today() - timedelta(days=100 * 365)
    data_de_nasc = st.date_input("Data de nascimento", datetime.today(),min_value= min_date.date()) 
    data_formatada = data_de_nasc.strftime("%Y-%m-%d")
   
if st.button("Cadastrar"):
    cadastro ={
    "email": email,
    "nome": nome,
    "senhaHashed": senha,
    "sobrenome": sobrenome,
    "telefoneCelular": telefone,
    "tipoUsuario": "cliente",
    "clienteTO":{
        "CPFCliente": cpf,
        "dataNascimento": data_formatada,
        "numeroCNH": cnh,
        "sexo": sexo
        },
    "oficinaTO": None
    }
    try:
        resposta_api = criar_cliente(cadastro)
        st.success("usuario cadastrado com sucesso")
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
    