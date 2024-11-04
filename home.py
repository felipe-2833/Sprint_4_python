import streamlit as st 
from modules.utils.utils import pula_linha   


st.set_page_config(page_title="Mecanico Virtual", page_icon="", layout="wide")

if "login" not in st.session_state:
    st.session_state["login"] = False
    
if "id" not in st.session_state:
    st.session_state["id"] = None
    
if "message_login" not in st.session_state:
    st.session_state["message_login"] = ""
    
if "messages" not in st.session_state:
    st.session_state.messages = []
    
if "carro" not in st.session_state:
    st.session_state.carro = ""
    
if "problema" not in st.session_state:
    st.session_state.problema = ""
    
if "status" not in st.session_state:
    st.session_state.status = False

initial_text = "A Wiz Solutions apresenta o \"Mecânico Virtual\", uma plataforma que facilita o diagnóstico de problemas veiculares por meio de um chatbot inteligente. Voltado para clientes e oficinas, o sistema permite que usuários relatem problemas, recebam diagnósticos precisos e obtenham orçamentos para serviços de reparo. As oficinas recebem detalhes completos dos clientes e dos diagnósticos, podendo organizar e otimizar o atendimento. Além disso, o aplicativo oferece um módulo de manutenção preventiva personalizada e suporte contínuo, promovendo uma comunicação direta e eficaz entre clientes e prestadores de serviços."
wiz_text = "A Wiz Soluções é uma equipe formada por estudantes apaixonados por tecnologia e inovação, com o objetivo de desenvolver soluções práticas e eficientes para desafios acadêmicos e do dia a dia. Criada por Andre Marcolongo, Felipe Fidelix e Samir Hage, a Wiz Soluções combina conhecimento e criatividade para oferecer projetos que aliam tecnologia de ponta e usabilidade. Nosso propósito é explorar novas ideias e transformar o aprendizado em ferramentas que agreguem valor e inovação."     
     
st.title("Mecâmico Virtual:")
st.write(initial_text)
st.header("Sobre Nos:")
st.write(wiz_text)
pula_linha(2)
st.write("ANDRÉ GERALDI MARCOLONGO - RM555285")
st.write("FELIPE LEVY STEPHENS FIDELIX - RM556426")
st.write("SAMIR HAGE NETO - RM557260")