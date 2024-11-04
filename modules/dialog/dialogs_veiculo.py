import streamlit as st 
from modules.database.veiculo import visualizar_veiculo, visualizar_modelo, visualizar_marca

@st.dialog("Infos User")
def info_veiculo(id:int):
    veiculo = visualizar_veiculo(id)
    id_modelo = veiculo["idModelo"]
    modelo = visualizar_modelo(id_modelo)
    id_marca = modelo["marcaIdMarca"]
    marca = visualizar_marca(id_marca)
    st.write(f"Marca: {marca["nomeMarca"]}")
    st.write(f"Modelo: {modelo["nomeModelo"]}")
    st.write(f"Placa: {veiculo["placaveiculo"]}")
    st.write(f"Motor: {veiculo["motor"]}")
    st.write(f"Combustivel: {veiculo["combustivel"]}")
    

