import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(page_title="Indicadores de Qualidade", layout="wide")

# --- FUNÇÃO PARA CARREGAR OS DADOS DO ARQUIVO CSV ---
@st.cache_data
def carregar_dados():
    """
    Carrega os dados das escolas a partir de um arquivo CSV local.
    """
    try:
        df = pd.read_csv('data/dados_escolas_es.csv', sep=';', decimal=',')
        return df
    except FileNotFoundError:
        return pd.DataFrame()

# Carrega os dados na inicialização da página
df_escolas = carregar_dados()

# --- LAYOUT DA PÁGINA ---
st.title("📈 Indicadores de Qualidade (IDEB & SAEB)")
st.markdown("Filtre por cidade e etapa de ensino para comparar os indicadores das escolas.")

st.write("") 

# --- CONTAINER DE FILTROS (BLOCO SUPERIOR) ---
with st.container(border=True):
    st.subheader("Filtros de Pesquisa")

    if df_escolas.empty:
        st.error("Arquivo 'data/dados_escolas_es.csv' não encontrado. Por favor, gere o arquivo e recarregue a página.")
    else:
        col1, col2 = st.columns(2)
        with col1:
            # Filtro de Cidade (populado dinamicamente)
            cidade = st.selectbox(
                "Selecione a cidade:",
                sorted(df_escolas['NO_MUNICIPIO'].unique().tolist()),
                index=None,
                placeholder="Escolha uma cidade"
            )
        
        with col2:
            st.markdown("**Etapa de Ensino:**")
            check_col1, check_col2 = st.columns(2)
            fundamental = check_col1.checkbox("Ensino Fundamental", key="fund_ind")
            medio = check_col2.checkbox("Ensino Médio", key="med_ind")

# --- LÓGICA DE FILTRAGEM ---
# Inicia com todos os dados e aplica os filtros selecionados
df_filtrado = df_escolas.copy()
if cidade:
    df_filtrado = df_filtrado[df_filtrado['NO_MUNICIPIO'] == cidade]
if fundamental:
    df_filtrado = df_filtrado[df_filtrado['IN_FUNDAMENTAL'] == 1]
if medio:
    df_filtrado = df_filtrado[df_filtrado['IN_MEDIO'] == 1]

st.write("") 

# --- CONTAINER DA TABELA DE DADOS (BLOCO INFERIOR) ---
with st.container(border=True):
    st.subheader("Resultados da Pesquisa")

    if df_escolas.empty:
        st.warning("Nenhum dado carregado.")
    else:
        # Define as colunas a serem exibidas na tabela principal
        colunas_tabela = [
            'NO_ENTIDADE', 'CO_ENTIDADE', 'MEDIA_SAEB_LP', 'MEDIA_SAEB_MT', 'IDEB_ANOS_FINAIS'
        ]
        st.dataframe(
            df_filtrado[colunas_tabela].rename(columns={
                'NO_ENTIDADE': 'Nome da Escola',
                'CO_ENTIDADE': 'Código INEP',
                'MEDIA_SAEB_LP': 'SAEB (Língua Portuguesa)',
                'MEDIA_SAEB_MT': 'SAEB (Matemática)',
                'IDEB_ANOS_FINAIS': 'IDEB (Anos Finais)'
            }),
            hide_index=True,
            use_container_width=True
        )
        st.caption(f"Exibindo {len(df_filtrado)} de {len(df_escolas)} escolas totais.")

st.write("")

# --- ANÁLISE DESCRITIVA (REQUISITO DA ETAPA 3) ---
with st.expander("**Clique aqui para ver a Análise Descritiva dos Dados da Tabela Acima**"):
    if df_filtrado.empty:
        st.warning("Nenhum dado para analisar. Selecione filtros acima para gerar a tabela.")
    else:
        # Seleciona apenas as colunas numéricas para a descrição estatística
        df_descritivo = df_filtrado[['MEDIA_SAEB_LP', 'MEDIA_SAEB_MT', 'IDEB_ANOS_FINAIS']].describe()
        st.dataframe(df_descritivo)
        st.markdown("""
        **Como interpretar a tabela:**
        - **count:** Número de escolas na amostra filtrada.
        - **mean:** A média das notas para cada indicador.
        - **std:** O desvio padrão, que indica o quão dispersas as notas estão em relação à média.
        - **min/max:** A menor e a maior nota encontrada no grupo.
        - **25% / 50% / 75%:** Os quartis. 50% é a mediana (a nota que divide o grupo ao meio).
        """)

