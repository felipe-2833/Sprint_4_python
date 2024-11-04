import streamlit as st 
from datetime import datetime, timedelta
import time
import json
import requests
from modules.database.usuario import visualizar_oficina, visualizar_user
from modules.database.chamados import criar_chamado, visualizar_chamados, apagar_chamado
from modules.database.veiculo import visualizar_veiculo

lista_veiculos = [visualizar_veiculo(920),visualizar_veiculo(1020), visualizar_veiculo(1100)]
lista_chamados = visualizar_chamados()
lista_meus_chamados = []
key_counter = 0
oficina = visualizar_oficina(89)
id_oficina = oficina["oficinaIdUser"]
nome_oficina = oficina["nomeOficina"]
match st.session_state.carro:
    case "Chevrolet - Onix":
        id_carro = 920
    case "Fiat - Argo":
        id_carro = 1020
    case "Chevrolet - Omega":
        id_carro = 1100
    case _:
        id_carro = 920
        


st.title("Chamados")

if st.session_state.id == None and st.session_state.login == False:
    st.error("Necessario fazer login para visualização dos veiculos.")
    
else:
    for chamado in lista_chamados:
        if chamado['clienteUserId'] == st.session_state.id:
            lista_meus_chamados.append(chamado)
    if st.session_state.status:
        with st.container(height=200):
            user = visualizar_user(st.session_state.id)
            nome = user["nome"]
            st.write(f"Nome: {nome}")
            st.write(f"Oficina: {nome_oficina}")
            st.write(f"Carro: {st.session_state.carro}")
            st.write(f"Problema: {st.session_state.problema}")
            
        
        if st.button("Gerar Chamado"):
            cadastro ={
                "clienteUserId": st.session_state.id,
                "dataAbertura": datetime.now().strftime("%Y-%m-%d"),
                "oficinaUserId": id_oficina,
                "status": "Aberto",
                "veiculoIdVeiculo": id_carro
            }
            
            try:
                resposta_api = criar_chamado(cadastro)
                st.success("Chamado gerado com sucesso")
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
    else:
        st.success("Por favor converse com o bot até o final para poder gerar um chamado!")
        
for chamado in lista_meus_chamados:
    id = chamado["idChamdo"]
    key_counter += 1
    with st.expander(f"Chamado {key_counter}"):
        st.write(f"Status: {chamado["status"]}")
        st.write(f"Data de abertura: {chamado["dataAbertura"]}")
        if st.button(label="Apagar",key=key_counter):
            apagar_chamado(id)
            st.success("Tarefa deletada com sucesso.")
            time.sleep(1)
            st.rerun()