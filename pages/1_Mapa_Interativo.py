import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página
st.set_page_config(page_title="Mapa das Escolas", layout="wide")

# Função para carregar os dados
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
st.title("📍 Mapa Interativo das Escolas")
st.markdown("Utilize os filtros para encontrar escolas específicas no mapa.")

col_filtro, col_mapa = st.columns([1, 3])

# --- FILTROS ---
with col_filtro:
    st.header("Filtros")

    if df_escolas.empty:
        st.error("Arquivo 'data/dados_escolas_es.csv' não encontrado.")
    else:
        # Filtro de Cidade
        lista_cidades = ["Todas"] + sorted(df_escolas['NO_MUNICIPIO'].unique().tolist())
        cidade_selecionada = st.selectbox("Selecione a cidade:", lista_cidades)

        df_filtrado = df_escolas.copy()
        if cidade_selecionada != "Todas":
            df_filtrado = df_filtrado[df_filtrado['NO_MUNICIPIO'] == cidade_selecionada]

        # SUGESTÃO IMPLEMENTADA: Filtro por Rede de Ensino
        lista_redes = sorted(df_filtrado['TP_DEPENDENCIA'].unique().tolist())
        redes_selecionadas = st.multiselect(
            "Selecione a rede de ensino:",
            lista_redes,
            default=lista_redes  # Deixa todas as redes selecionadas por padrão
        )

        if redes_selecionadas:
            df_filtrado = df_filtrado[df_filtrado['TP_DEPENDENCIA'].isin(redes_selecionadas)]
        else:
            df_filtrado = pd.DataFrame() # Limpa o dataframe se nada for selecionado

        # Filtro de Escola
        lista_escolas = ["Todas"] + sorted(df_filtrado['NO_ENTIDADE'].unique().tolist())
        escola_selecionada = st.selectbox("Selecione a escola:", lista_escolas)

        if escola_selecionada != "Todas":
            df_filtrado = df_filtrado[df_filtrado['NO_ENTIDADE'] == escola_selecionada]

        st.write(f"**{len(df_filtrado)} escolas encontradas.**")

# --- MAPA ---
with col_mapa:
    st.header("Mapa de Localização")

    if df_filtrado.empty:
        st.warning("Nenhuma escola para exibir. Verifique os filtros.")
    else:
        fig = px.scatter_mapbox(
            df_filtrado,
            lat="LATITUDE",
            lon="LONGITUDE",
            hover_name="NO_ENTIDADE",
            hover_data={"TP_DEPENDENCIA": True, "CO_ENTIDADE": True, "LATITUDE": False, "LONGITUDE": False},
            color="TP_DEPENDENCIA",
            color_discrete_map={
                "Estadual": "#0044ff",
                "Municipal": "#29a329",
                "Privada": "#ff3333"
            },
            zoom=10 if cidade_selecionada != "Todas" and len(df_filtrado) > 0 else 8,
            center={"lat": df_filtrado.LATITUDE.mean(), "lon": df_filtrado.LONGITUDE.mean()},
            height=600
        )
        fig.update_layout(
            mapbox_style="open-street-map",
            margin={"r":0,"t":0,"l":0,"b":0},
            legend_title_text='Rede de Ensino'
        )
        st.plotly_chart(fig, use_container_width=True)
