import streamlit as st 
import pandas as pd
import time
from modules.utils.utils import pula_linha

initial_text = "A Wiz Solutions apresenta o \"Mecânico Virtual\", uma plataforma que facilita o diagnóstico de problemas veiculares por meio de um chatbot inteligente. Voltado para clientes e oficinas, o sistema permite que usuários relatem problemas, recebam diagnósticos precisos e obtenham orçamentos para serviços de reparo. As oficinas recebem detalhes completos dos clientes e dos diagnósticos, podendo organizar e otimizar o atendimento. Além disso, o aplicativo oferece um módulo de manutenção preventiva personalizada e suporte contínuo, promovendo uma comunicação direta e eficaz entre clientes e prestadores de serviços."
wiz_text = "A Wiz Soluções é uma equipe formada por estudantes apaixonados por tecnologia e inovação, com o objetivo de desenvolver soluções práticas e eficientes para desafios acadêmicos e do dia a dia. Criada por Andre Marcolongo, Felipe Fidelix e Samir Hage, a Wiz Soluções combina conhecimento e criatividade para oferecer projetos que aliam tecnologia de ponta e usabilidade. Nosso propósito é explorar novas ideias e transformar o aprendizado em ferramentas que agreguem valor e inovação."     
     
def stream_data(text):
    for word in text.split(" "):
        yield word + " "
        time.sleep(0.02)
        
def chatbot():
    st.title("Mecânico IA:")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    for message in st.session_state.messages:
        with st.chat_message(message["tipo_bot"]):
            st.markdown(message["conteudo"])
    
    if prompt := st.chat_input("Digite aqui..."):
        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state.messages.append({"tipo_bot": "user", "conteudo": prompt})
        
        response = f"echo: {prompt}"
        with st.chat_message("assistant"):
            st.markdown(stream_data(response))
        st.session_state.messages.append({"tipo_bot": "assistant", "conteudo": response})
    