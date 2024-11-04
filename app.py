import streamlit as st 
import pandas as pd
from modules.utils.utils import pula_linha   
from pages.home import home
from pages.chatbot import chatbot


pg = st.navigation([
    st.Page(home, title="First page", icon="🔥"),
    st.Page(chatbot, title="Second page", icon=":material/favorite:"),
])
pg.run()