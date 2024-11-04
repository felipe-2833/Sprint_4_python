# Mecânixo Virtual

O foco do projeto é o diagnóstico digital, impulsionado por um assistente
virtual (chatbot), que permite aos usuários relatarem os problemas enfrentados com
seus veículos. A Inteligência Artificial assume o papel do mecânico, agilizando o
processo ao fornecer diagnósticos precisos e encaminhando-os aos profissionais
responsáveis.


## Funcionalidades

- **Criar Tarefas:** Permite a criação de novas tarefas com informações detalhadas, como título, descrição, data de vencimento e prioridade.

- **Atualizar Tarefas:** O sistema permite a edição das tarefas existentes, ajustando campos como descrição, status, prioridade ou outro que seja.

- **Excluir Tarefas:** Possibilidade de remover tarefas quando concluídas ou não mais necessárias.

- **Listagem de Tarefas:** Visualização de todas as tarefas criadas, filtradas por status, prioridade ou data.

- **Banco de Dados Oracle:** Todas as informações são armazenadas e manipuladas através de uma conexão com o OracleDB, garantindo persistência e segurança dos dados.

- **Sistema de notificação por email:** Receba no seu email as notificações sobre suas tarefas.

- **Relatório:** Relatório sobre as tarefas pendentes, em andamento e concluídas.

## Requisitos

- Python 3.x
- oracledb

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/felipe-2833/Sprint_4_python.git
```

2. Instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

3. Execute a API no terminal:

```bash
cd api
fastapi dev api.py
```

4. Execute a GUI em outro terminal:
```bash
streamlit run main.py
```

Não esqueça de conferir os caminhos (path), para rodar os comandos inicializando a aplicação da forma correta!

## Equipe

- André Geraldi Marcolongo - **RM: 555285**
- Felipe Levy Stephens Fidelix - **RM: 556426**
- Samir Hage Neto - **RM: 557260**

