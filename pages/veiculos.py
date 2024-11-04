import streamlit as st 
from datetime import datetime, timedelta
import time
import json
import requests
from modules.utils.utils import pula_linha
from modules.database.veiculo import visualizar_veiculo, visualizar_modelo, visualizar_marca
from modules.dialog.dialogs_veiculo import info_veiculo

lista_veiculos = [visualizar_veiculo(920),visualizar_veiculo(1020), visualizar_veiculo(1100)]
key_counter = 0


st.title("Veiculos")

if st.session_state.id == None and st.session_state.login == False:
    st.error("Necessario fazer login para visualização dos veiculos.")
else:
    for veiculo in lista_veiculos:
        id = veiculo["idVeiculo"]
        id_modelo = veiculo["idModelo"]
        modelo = visualizar_modelo(id_modelo)
        id_marca = modelo["marcaIdMarca"]
        marca = visualizar_marca(id_marca)
        with st.expander(f"{marca['nomeMarca']} - {modelo['nomeModelo']}"):
            key_counter += 1
            if st.button(label="Infos",key=key_counter):
                info_veiculo(id)
            
            
            
    
    