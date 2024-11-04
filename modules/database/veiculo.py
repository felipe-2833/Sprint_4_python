import requests

def visualizar_veiculos() -> list[dict]:
    url = "http://localhost:8080/mecanico/veiculo"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def visualizar_veiculo(id:int) -> dict:
    url = f"http://localhost:8080/mecanico/veiculo/{id}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()



def visualizar_modelo(id:int) -> dict:
    url = f"http://localhost:8080/mecanico/modelo/{id}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def visualizar_marca(id:int) -> dict:
    url = f"http://localhost:8080/mecanico/marca/{id}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
