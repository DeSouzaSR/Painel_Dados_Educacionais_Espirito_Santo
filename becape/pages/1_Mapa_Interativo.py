import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página para usar a largura total
st.set_page_config(page_title="Mapa das Escolas", layout="wide")

# --- FUNÇÃO PARA CARREGAR OS DADOS DO ARQUIVO CSV ---
# O decorador @st.cache_data garante que o arquivo CSV seja lido apenas uma vez,
# melhorando a performance da aplicação.
@st.cache_data
def carregar_dados():
    """
    Carrega os dados das escolas a partir de um arquivo CSV local.
    """
    try:
        df = pd.read_csv('data/dados_escolas_es.csv', sep=';', decimal=',')
        return df
    except FileNotFoundError:
        # Retorna um DataFrame vazio se o arquivo não for encontrado,
        # evitando que o app quebre.
        return pd.DataFrame()

# Carrega os dados na inicialização da página
df_escolas = carregar_dados()

# --- LAYOUT DA PÁGINA ---
st.title("📍 Mapa Interativo das Escolas")
st.markdown("Utilize os filtros à esquerda para encontrar escolas específicas no mapa.")

# --- CRIAÇÃO DO LAYOUT EM COLUNAS ---
col_filtro, col_mapa = st.columns([1, 3])

# --- CONTAINER DE FILTROS (LADO ESQUERDO) ---
with col_filtro:
    st.header("Filtros")

    # Verifica se os dados foram carregados corretamente
    if df_escolas.empty:
        st.error("Arquivo 'data/dados_escolas_es.csv' não encontrado. Por favor, gere o arquivo e recarregue a página.")
    else:
        # Filtro de Cidade (populado dinamicamente com os dados do CSV)
        lista_cidades = ["Todas"] + sorted(df_escolas['NO_MUNICIPIO'].unique().tolist())
        cidade_selecionada = st.selectbox(
            "Selecione a cidade:",
            lista_cidades
        )

        # Filtra o DataFrame com base na cidade selecionada
        if cidade_selecionada != "Todas":
            df_filtrado = df_escolas[df_escolas['NO_MUNICIPIO'] == cidade_selecionada]
        else:
            df_filtrado = df_escolas

        # Filtro de Escola (populado com base na cidade já filtrada)
        lista_escolas = ["Todas"] + sorted(df_filtrado['NO_ENTIDADE'].unique().tolist())
        escola_selecionada = st.selectbox(
            "Selecione a escola:",
            lista_escolas
        )

        # Filtra novamente o DataFrame com base na escola selecionada
        if escola_selecionada != "Todas":
            df_filtrado = df_filtrado[df_filtrado['NO_ENTIDADE'] == escola_selecionada]

        st.write(f"**{len(df_filtrado)} escolas encontradas.**")


# --- CONTAINER DO MAPA (LADO DIREITO) ---
with col_mapa:
    st.header("Mapa de Localização")

    # Garante que o mapa só seja renderizado se houver dados
    if df_escolas.empty or df_filtrado.empty:
        st.warning("Nenhuma escola para exibir. Verifique os filtros ou o arquivo de dados.")
    else:
        # Cria o mapa interativo com Plotly Express usando os dados filtrados
        fig = px.scatter_mapbox(
            df_filtrado,
            lat="LATITUDE",
            lon="LONGITUDE",
            hover_name="NO_ENTIDADE", # O que aparece ao passar o mouse
            hover_data={
                "TP_DEPENDENCIA": True, # Mostra a rede de ensino
                "CO_ENTIDADE": True,    # Mostra o código INEP
                "LATITUDE": False,      # Oculta a latitude no popup
                "LONGITUDE": False      # Oculta a longitude no popup
            },
            color="TP_DEPENDENCIA", # Colore os pontos pela rede de ensino
            color_discrete_map={    # Define cores específicas para cada rede
                "Estadual": "#0044ff",
                "Municipal": "#29a329",
                "Privada": "#ff3333"
            },
            # O zoom e o centro do mapa se ajustam dinamicamente
            zoom=10 if cidade_selecionada != "Todas" else 8,
            center={"lat": df_filtrado.LATITUDE.mean(), "lon": df_filtrado.LONGITUDE.mean()},
            height=600
        )

        fig.update_layout(
            mapbox_style="open-street-map",
            margin={"r":0,"t":0,"l":0,"b":0},
            legend_title_text='Rede de Ensino'
        )
        st.plotly_chart(fig, use_container_width=True)

