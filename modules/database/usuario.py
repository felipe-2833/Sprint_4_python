import streamlit as st 
import requests
import json
from datetime import datetime 

def criar_cliente(data:dict) -> dict:
    url = "http://localhost:8080/mecanico/usuario"
    response = requests.post(url,json=data)
    response.raise_for_status()
    return response.json()

def visualizar() -> list[dict]:
    url = "http://localhost:8080/mecanico/usuario"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def visualizar_user(id:int) -> dict:
    url = f"http://localhost:8080/mecanico/usuario/{id}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def visualizar_cliente(id:int) -> dict:
    url = f"http://localhost:8080/mecanico/cliente/{id}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def atualiza_user(id:int, data:dict):
    url = f"http://localhost:8080/mecanico/usuario/{id}"
    response = requests.put(url, json=data)
    response.raise_for_status()
    return response.json()

def atualiza_cliente(id:int, data:dict):
    url = f"http://localhost:8080/mecanico/cliente/{id}"
    response = requests.put(url, json=data)
    response.raise_for_status()
    return response.json()