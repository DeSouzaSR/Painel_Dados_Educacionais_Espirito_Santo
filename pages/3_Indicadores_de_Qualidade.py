import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página
st.set_page_config(page_title="Indicadores de Qualidade", layout="wide")

# Função para carregar dados
@st.cache_data
def carregar_dados():
    try:
        df = pd.read_csv('data/dados_escolas_es.csv', sep=';', decimal=',')
        return df
    except FileNotFoundError:
        return pd.DataFrame()

# Carrega os dados
df_escolas = carregar_dados()

# --- LAYOUT DA PÁGINA ---
st.title("📈 Indicadores de Qualidade e Análise Comparativa")
st.markdown("Filtre por cidade e etapa para comparar os indicadores das escolas.")
st.write("")

# --- FILTROS ---
with st.container(border=True):
    st.subheader("Filtros de Pesquisa")
    if df_escolas.empty:
        st.error("Arquivo 'data/dados_escolas_es.csv' não encontrado.")
    else:
        col1, col2 = st.columns(2)
        with col1:
            cidade = st.selectbox("Selecione a cidade:", ["Todas"] + sorted(df_escolas['NO_MUNICIPIO'].unique().tolist()))
        with col2:
            st.markdown("**Etapa de Ensino:**")
            check_col1, check_col2 = st.columns(2)
            fundamental = check_col1.checkbox("Ensino Fundamental", key="fund_ind")
            medio = check_col2.checkbox("Ensino Médio", key="med_ind")

# --- LÓGICA DE FILTRAGEM ---
df_filtrado = df_escolas.copy()
if cidade and cidade != "Todas":
    df_filtrado = df_filtrado[df_filtrado['NO_MUNICIPIO'] == cidade]
if fundamental:
    df_filtrado = df_filtrado[df_filtrado['IN_FUNDAMENTAL'] == 1]
if medio:
    df_filtrado = df_filtrado[df_filtrado['IN_MEDIO'] == 1]

# --- TABELA DE RESULTADOS ---
with st.container(border=True):
    st.subheader("Resultados da Pesquisa")
    if df_filtrado.empty:
        st.warning("Nenhuma escola encontrada para os filtros selecionados.")
    else:
        colunas_tabela = ['NO_ENTIDADE', 'TP_DEPENDENCIA', 'MEDIA_SAEB_LP', 'MEDIA_SAEB_MT', 'IDEB_ANOS_FINAIS']
        st.dataframe(df_filtrado[colunas_tabela].rename(columns={'NO_ENTIDADE': 'Nome da Escola', 'TP_DEPENDENCIA': 'Rede', 'MEDIA_SAEB_LP': 'SAEB (LP)', 'MEDIA_SAEB_MT': 'SAEB (MT)', 'IDEB_ANOS_FINAIS': 'IDEB'}), hide_index=True, use_container_width=True)
        st.caption(f"Exibindo {len(df_filtrado)} de {len(df_escolas)} escolas totais.")

# --- SUGESTÃO IMPLEMENTADA: GRÁFICOS COMPARATIVOS POR REDE ---
st.write("")
st.subheader(f"Análise Comparativa por Rede de Ensino em '{cidade}'")
with st.container(border=True):
    if df_filtrado.empty:
        st.info("Selecione filtros para gerar a análise comparativa.")
    else:
        # Agrupa os dados por rede e calcula as médias
        df_rede = df_filtrado.groupby('TP_DEPENDENCIA')[['MEDIA_SAEB_LP', 'MEDIA_SAEB_MT', 'IDEB_ANOS_FINAIS']].mean().reset_index()

        graf1, graf2 = st.columns(2)
        with graf1:
            st.markdown("##### Média SAEB por Rede")
            fig_saeb = px.bar(df_rede, x='TP_DEPENDENCIA', y=['MEDIA_SAEB_LP', 'MEDIA_SAEB_MT'], barmode='group', labels={'TP_DEPENDENCIA': 'Rede de Ensino', 'value': 'Nota Média SAEB'}, title="SAEB: Língua Portuguesa vs. Matemática")
            st.plotly_chart(fig_saeb, use_container_width=True)
        with graf2:
            st.markdown("##### Média IDEB por Rede")
            fig_ideb = px.bar(df_rede, x='TP_DEPENDENCIA', y='IDEB_ANOS_FINAIS', labels={'TP_DEPENDENCIA': 'Rede de Ensino', 'IDEB_ANOS_FINAIS': 'Nota Média IDEB'}, title="IDEB (Anos Finais)")
            st.plotly_chart(fig_ideb, use_container_width=True)

# --- ANÁLISE DESCRITIVA ---
with st.expander("**Clique para ver a Análise Descritiva dos Dados Filtrados**"):
    if not df_filtrado.empty:
        st.dataframe(df_filtrado[['MEDIA_SAEB_LP', 'MEDIA_SAEB_MT', 'IDEB_ANOS_FINAIS']].describe())
