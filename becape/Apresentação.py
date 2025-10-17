import streamlit as st

# Configuração da página (mantém a mesma)
st.set_page_config(
    page_title="Início",
    page_icon="📚",
    layout="wide"
)

# Título e descrição (continuam no topo, sem container)
st.title("📚 Painel de Dados Educacionais do Espírito Santo")
st.markdown("""
Esta aplicação apresenta um MVP (Produto Mínimo Viável) como parte da avaliação da disciplina de Cloud Computing 
para produtos de dados na Pós-graduação em Mineração de Dados.

- Professor: Maxwell Monteiro
- Aluno: Sandro Ricardo De Souza
""")

# CSS para definir o estilo dos containers. Isso cria uma classe chamada .custom-container com borda, cantos arredondados e espaçamento.
st.markdown("""
<style>
.custom-container {
    border: 1px solid #e6e6e6;       /* Cor suave da borda */
    border-radius: 10px;             /* Cantos arredondados */
    padding: 25px;                   /* Espaçamento interno */
    height: 100%;                    /* Garante que os containers na mesma linha tenham a mesma altura */
    background-color: #fafafa;       /* Cor de fundo sutil para destacar */
}
.custom-container h3 {
    margin-top: 0;                   /* Remove a margem superior do título */
}
</style>
""", unsafe_allow_html=True)

# Duas colunas para posicionar os containers lado a lado.
col1, col2 = st.columns(2)

# Primeiro container na primeira coluna. 
# st.markdown para criar uma div HTML aplicado à classe custom-container.
with col1:
    st.markdown("""
    <div class="custom-container">
        <h3>Objetivo do Projeto</h3>
        <p>
        O objetivo é criar um painel interativo para visualização e análise de dados sobre as escolas do estado do Espírito Santo. 
        A aplicação permite explorar as escolas em um mapa, visualizar estatísticas detalhadas e consultar indicadores 
        de qualidade educacional, como o IDEB.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Segundo container na segunda coluna.
with col2:
    st.markdown("""
    <div class="custom-container">
        <h3>Fonte dos Dados</h3>
        <p>
        Os dados utilizados neste projeto são públicos e foram obtidos através do portal de microdados do 
        Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP). Foram utilizados 
        principalmente os dados do Censo Escolar e os resultados do Índice de Desenvolvimento da Educação Básica (Ideb).
        </p>
    </div>
    """, unsafe_allow_html=True)

st.write("") # Adiciona um pequeno espaço vertical antes do texto final

# Texto final (continua embaixo, sem container)
st.info("Navegue pelas seções no menu à esquerda para explorar os dados.")
