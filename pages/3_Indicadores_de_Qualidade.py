import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(page_title="Indicadores de Qualidade", layout="wide")

st.title("📈 Indicadores de Qualidade (IDEB & SAEB)")
st.markdown("Filtre por cidade e etapa de ensino para comparar os indicadores das escolas.")

st.write("") # Adiciona um espaço vertical

# --- CONTAINER DE FILTROS (BLOCO SUPERIOR) ---
# Usamos st.container(border=True) para criar a caixa com bordas arredondadas
with st.container(border=True):
    st.subheader("Filtros de Pesquisa")

    # Criamos colunas para organizar os filtros de forma limpa
    col1, col2, col3 = st.columns([2, 2, 1])

    with col1:
        # Filtro de Cidade
        cidade = st.selectbox(
            "Selecione a cidade:",
            ["Vitória", "Vila Velha", "Serra", "Cariacica"],
            index=None,
            placeholder="Escolha uma cidade"
        )
    
    with col2:
        st.markdown("**Etapa de Ensino:**")
        # Colunas internas para os checkboxes ficarem lado a lado
        check_col1, check_col2 = st.columns(2)
        with check_col1:
            ensino_fundamental = st.checkbox("Ensino Fundamental", key="fund_ind")
        with check_col2:
            ensino_medio = st.checkbox("Ensino Médio", key="med_ind")

    with col3:
        # Espaço para alinhar o botão verticalmente
        st.write("")
        st.write("")
        st.button("Limpar Filtros", use_container_width=True)

st.write("") # Espaço entre os dois containers

# --- CONTAINER DA TABELA DE DADOS (BLOCO INFERIOR) ---
with st.container(border=True):
    st.subheader("Resultados da Pesquisa")

    # --- DADOS FICTÍCIOS PARA A TABELA ---
    # Criamos um DataFrame do Pandas para simular os dados que virão do INEP
    dados_ficticios = {
        "Nome da Escola": [
            "EMEF Exemplo de Vitória",
            "EEEFM Modelo da Serra",
            "Escola Fictícia de Vila Velha"
        ],
        "Código INEP": [32012345, 32054321, 32098765],
        "Nota SAEB": [275.4, 290.1, 260.8],
        "Nota IDEB": [6.8, 7.1, 6.2]
    }
    df_ficticio = pd.DataFrame(dados_ficticios)

    # Exibimos a tabela usando st.dataframe
    st.dataframe(
        df_ficticio,
        use_container_width=True, # Tabela usa a largura total do container
        hide_index=True # Esconde o índice numérico da tabela
    )
    st.caption("A tabela será preenchida com dados reais de acordo com os filtros na próxima etapa.")
