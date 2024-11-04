import streamlit as st 

#Função para pular linhas dependendo do numero passado
def pula_linha(n:int):
    for i in range(0,n):
        st.write(" ")