import streamlit as st 
import requests
import json
from datetime import datetime 

def criar_chamado(data:dict) -> dict:
    url = "http://localhost:8080/mecanico/chamado"
    response = requests.post(url,json=data)
    response.raise_for_status()
    return response.json()

def visualizar_chamados() -> list[dict]:
    url = "http://localhost:8080/mecanico/chamado"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def apagar_chamado(id:int):
    url = f"http://localhost:8080/mecanico/chamado/{id}"
    response = requests.delete(url)
    response.raise_for_status()