# app.py

import streamlit as st
from streamlit.web.server.server import Server

# Esta é a configuração da página que será mostrada ANTES do menu ser selecionado
st.set_page_config(
    page_title="Início",
    page_icon="📚",
    layout="wide"
)

st.title("Bem-vindo ao Painel Educacional do ES")
st.sidebar.success("Selecione uma das páginas acima.")

st.markdown(
    """
    Este projeto apresenta dados sobre as escolas do Espírito Santo.
    **👈 Selecione uma das opções no menu lateral** para começar a explorar.
    ### Quer saber mais?
    - Confira a página de **Apresentação** para detalhes do projeto.
    - Explore o **Mapa Interativo** para localizar as escolas.
    """
)
