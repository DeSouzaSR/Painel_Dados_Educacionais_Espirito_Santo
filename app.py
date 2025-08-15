import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Painel Educacional - ES",
    page_icon="📚",
    layout="wide"
)

# Título e descrição
st.title("📚 Painel de Dados Educacionais do Espírito Santo")

st.markdown("""
Esta aplicação apresenta um MVP (Produto Mínimo Viável) como parte da avaliação da disciplina de Cloud Computing 
para produtos de dados na Pós-graduação em Mineração de Dados.
""")

st.subheader("Objetivo do Projeto")
st.write("""
O objetivo é criar um painel interativo para visualização e análise de dados sobre as escolas do estado do Espírito Santo. 
A aplicação permite explorar as escolas em um mapa, visualizar estatísticas detalhadas e consultar indicadores 
de qualidade educacional, como o IDEB.
""")

st.subheader("Fonte dos Dados")
st.write("""
Os dados utilizados neste projeto são públicos e foram obtidos através do portal de microdados do 
Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP). Foram utilizados 
principalmente os dados do Censo Escolar e os resultados do Índice de Desenvolvimento da Educação Básica (Ideb).
""")

st.info("Navegue pelas seções no menu à esquerda para explorar os dados.")
