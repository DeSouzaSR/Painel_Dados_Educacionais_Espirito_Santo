import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página para usar a largura total
st.set_page_config(page_title="Mapa das Escolas", layout="wide")

st.title("📍 Mapa Interativo das Escolas")
st.markdown("Utilize os filtros à esquerda para encontrar escolas específicas no mapa.")

# --- CRIAÇÃO DO LAYOUT ---
# Duas colunas: 1 parte para filtros, 3 para o mapa
col_filtro, col_mapa = st.columns([1, 3])

# --- CONTAINER DE FILTROS (1/4 da tela) ---
with col_filtro:
    st.header("Filtros")

    # Widgets de filtro com opções de exemplo (Não têm funcionalidade)
    cidade_selecionada = st.selectbox(
        "Selecione a cidade:",
        ["Vitória", "Vila Velha", "Serra", "Cariacica", "Guarapari"],
        index=None, # Faz o campo começar vazio
        placeholder="Escolha uma cidade"
    )

    escola_selecionada = st.selectbox(
        "Selecione a escola:",
        ["Primeiro, selecione uma cidade"], # Mensagem de exemplo
        disabled=True # Desabilitado para indicar que depende da cidade
    )

    st.write("") # Adiciona um espaço vertical

    # Botão para limpar os filtros
    st.button("Limpar Filtros", use_container_width=True)

    st.caption("Observação: Os filtros estarão funcionais na próxima etapa do projeto.")


# --- CONTAINER DO MAPA (3/4 da tela) ---
with col_mapa:
    st.header("Mapa de Localização")

    # --- MAPA PLACEHOLDER (MAPA DO BRASIL) ---
    # Dados de algumas capitais apenas para preencher o mapa visualmente
    dados_brasil = {
        'Capital': ['Vitória', 'São Paulo', 'Rio de Janeiro', 'Brasília', 'Salvador'],
        'lat': [-20.3155, -23.5505, -22.9068, -15.7801, -12.9747],
        'lon': [-40.3128, -46.6333, -43.1729, -47.9292, -38.4767]
    }
    df_brasil = pd.DataFrame(dados_brasil)

    # Figura do mapa com Plotly, centrado no Brasil
    fig = px.scatter_mapbox(
        df_brasil,
        lat="lat",
        lon="lon",
        hover_name="Capital",
        color_discrete_sequence=["#0044ff"], # Cor dos pontos
        zoom=3.5, # Zoom para mostrar o Brasil
        center={"lat": -14.2350, "lon": -51.9253}, # Centro geográfico do Brasil
        height=600
    )

    # Atualização do estilo do mapa
    fig.update_layout(
        mapbox_style="open-street-map",
        margin={"r":0,"t":0,"l":0,"b":0}
    )

    # Exibição do mapa no Streamlit
    st.plotly_chart(fig, use_container_width=True)
