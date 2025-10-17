import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Configuração da página
st.set_page_config(page_title="Estatísticas", layout="wide")

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
st.title("📊 Estatísticas da Escola")
st.markdown("Filtre e selecione uma escola para visualizar seus dados e compará-los com a média municipal.")

col_filtro, col_dados = st.columns([1, 3])

# --- FILTROS ---
with col_filtro:
    st.header("Filtros")
    if df_escolas.empty:
        st.error("Arquivo 'data/dados_escolas_es.csv' não encontrado.")
    else:
        cidade = st.selectbox(
            "Selecione a cidade:", 
            sorted(df_escolas['NO_MUNICIPIO'].unique().tolist()), 
            index=None, 
            placeholder="Escolha uma cidade"
        )
        
        df_filtrado_escolas = df_escolas.copy()
        if cidade:
            df_filtrado_escolas = df_escolas[df_escolas['NO_MUNICIPIO'] == cidade]

        fundamental = st.checkbox("Ensino Fundamental")
        medio = st.checkbox("Ensino Médio")
        if fundamental:
            df_filtrado_escolas = df_filtrado_escolas[df_filtrado_escolas['IN_FUNDAMENTAL'] == 1]
        if medio:
            df_filtrado_escolas = df_filtrado_escolas[df_filtrado_escolas['IN_MEDIO'] == 1]

        escola_selecionada = st.selectbox(
            "Selecione a escola:", 
            sorted(df_filtrado_escolas['NO_ENTIDADE'].unique().tolist()), 
            index=None, 
            placeholder="Selecione uma escola"
        )

# --- PAINEL DE DADOS ---
with col_dados:
    if not escola_selecionada:
        st.info("👈 Por favor, selecione uma escola no painel de filtros para visualizar os detalhes.")
    else:
        # Pega os dados da escola selecionada
        dados_escola = df_escolas[df_escolas['NO_ENTIDADE'] == escola_selecionada].iloc[0]
        cidade_escola = dados_escola['NO_MUNICIPIO']
        
        # Calcula as médias do município para comparação
        media_cidade = df_escolas[df_escolas['NO_MUNICIPIO'] == cidade_escola]
        media_saeb_lp_cidade = round(media_cidade['MEDIA_SAEB_LP'].mean(), 2)
        media_saeb_mt_cidade = round(media_cidade['MEDIA_SAEB_MT'].mean(), 2)
        media_ideb_cidade = round(media_cidade['IDEB_ANOS_FINAIS'].mean(), 2)

        # Exibe informações básicas da escola
        with st.container(border=True):
            st.markdown(f"### {dados_escola['NO_ENTIDADE']}")
            st.write(f"**Cidade:** {dados_escola['NO_MUNICIPIO']}")
            info1, info2, info3 = st.columns(3)
            info1.metric("Código INEP", dados_escola['CO_ENTIDADE'])
            info2.metric("Rede de Ensino", dados_escola['TP_DEPENDENCIA'])
            etapas = [("Fundamental" if dados_escola['IN_FUNDAMENTAL'] == 1 else None), ("Médio" if dados_escola['IN_MEDIO'] == 1 else None)]
            info3.metric("Etapas Ofertadas", ", ".join(filter(None, etapas)))
        
        st.write("")
        st.subheader("Gráficos de Desempenho Comparativo")
        
        graf1, graf2 = st.columns(2)
        
        with graf1:
            st.markdown("##### **Notas Médias - SAEB**")
            # SUGESTÃO IMPLEMENTADA: Gráfico de barras agrupadas com Plotly
            fig_saeb = go.Figure(data=[
                go.Bar(name='Nota da Escola', x=['Língua Portuguesa', 'Matemática'], y=[dados_escola['MEDIA_SAEB_LP'], dados_escola['MEDIA_SAEB_MT']]),
                go.Bar(name=f'Média de {cidade_escola}', x=['Língua Portuguesa', 'Matemática'], y=[media_saeb_lp_cidade, media_saeb_mt_cidade])
            ])
            fig_saeb.update_layout(
                barmode='group', 
                legend_title_text='Comparativo', 
                yaxis_title="Nota SAEB",
                xaxis_title="Componente"
            )
            st.plotly_chart(fig_saeb, use_container_width=True)

        with graf2:
            st.markdown(f"##### **Nota - IDEB (vs. Média de {cidade_escola})**")
            # Usar st.metric com o parâmetro 'delta' para uma comparação direta
            st.metric(
                label="IDEB da Escola", 
                value=dados_escola['IDEB_ANOS_FINAIS'], 
                delta=round(dados_escola['IDEB_ANOS_FINAIS'] - media_ideb_cidade, 2),
                help=f"A média do IDEB para as escolas de {cidade_escola} é {media_ideb_cidade}."
            )
            st.caption("O 'delta' indica a diferença em relação à média do município.")

