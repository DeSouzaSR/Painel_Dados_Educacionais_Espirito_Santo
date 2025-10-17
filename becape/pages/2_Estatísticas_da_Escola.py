import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(page_title="Estatísticas", layout="wide")

# --- FUNÇÃO PARA CARREGAR OS DADOS DO ARQUIVO CSV ---
@st.cache_data
def carregar_dados():
    try:
        df = pd.read_csv('data/dados_escolas_es.csv', sep=';', decimal=',')
        return df
    except FileNotFoundError:
        return pd.DataFrame()

# Carrega os dados na inicialização da página
df_escolas = carregar_dados()

# --- LAYOUT DA PÁGINA ---
st.title("📊 Estatísticas das Escolas")
st.markdown("Filtre e selecione uma escola para visualizar seus dados detalhados e gráficos de desempenho.")

col_filtro, col_dados = st.columns([1, 3])

# --- CONTAINER DE FILTROS (LADO ESQUERDO) ---
with col_filtro:
    st.header("Filtros")

    if df_escolas.empty:
        st.error("Arquivo 'data/dados_escolas_es.csv' não encontrado. Por favor, gere o arquivo e recarregue a página.")
    else:
        # Filtro de Cidade
        cidade = st.selectbox(
            "Selecione a cidade:",
            sorted(df_escolas['NO_MUNICIPIO'].unique().tolist()),
            index=None,
            placeholder="Escolha uma cidade"
        )
        
        df_filtrado = df_escolas.copy()
        if cidade:
            df_filtrado = df_escolas[df_escolas['NO_MUNICIPIO'] == cidade]

        # Filtros de Etapa de Ensino
        st.markdown("**Etapa de Ensino:**")
        fundamental = st.checkbox("Ensino Fundamental")
        medio = st.checkbox("Ensino Médio")
        if fundamental:
            df_filtrado = df_filtrado[df_filtrado['IN_FUNDAMENTAL'] == 1]
        if medio:
            df_filtrado = df_filtrado[df_filtrado['IN_MEDIO'] == 1]

        # Filtro de Escola
        escola_selecionada = st.selectbox(
            "Selecione a escola:",
            sorted(df_filtrado['NO_ENTIDADE'].unique().tolist()),
            index=None,
            placeholder="Selecione uma escola nos filtros"
        )

# --- PAINEL DE DADOS (LADO DIREITO) ---
with col_dados:
    if not escola_selecionada:
        st.info("👈 Por favor, selecione uma escola no painel de filtros para visualizar os detalhes.")
    else:
        dados_escola = df_escolas[df_escolas['NO_ENTIDADE'] == escola_selecionada].iloc[0]

        with st.container(border=True):
            st.markdown(f"### {dados_escola['NO_ENTIDADE']}")
            st.write(f"**Cidade:** {dados_escola['NO_MUNICIPIO']}")
            st.write(f"**Endereço:** {dados_escola['DS_ENDERECO']}")
            
            info1, info2, info3 = st.columns(3)
            info1.metric("Código INEP", dados_escola['CO_ENTIDADE'])
            info2.metric("Rede de Ensino", dados_escola['TP_DEPENDENCIA'])
            
            etapas = []
            if dados_escola['IN_FUNDAMENTAL'] == 1: etapas.append("Fundamental")
            if dados_escola['IN_MEDIO'] == 1: etapas.append("Médio")
            info3.metric("Etapas Ofertadas", ", ".join(etapas))

        st.write("") 

        st.subheader("Gráficos de Desempenho")
        
        graf1, graf2 = st.columns(2)
        
        with graf1:
            st.markdown("##### Notas Médias - SAEB")
            
            # --- CÓDIGO CORRIGIDO ---
            # 1. Crie um DataFrame com as notas em colunas separadas
            df_saeb_chart = pd.DataFrame({
                "Língua Portuguesa": [dados_escola['MEDIA_SAEB_LP']],
                "Matemática": [dados_escola['MEDIA_SAEB_MT']]
            })

            # 2. Use st.bar_chart. Agora você tem 2 colunas e 2 cores, o que funciona.
            st.bar_chart(
                df_saeb_chart,
                color=["#FF4B4B", "#0044FF"] 
            )

        with graf2:
            st.markdown("##### Nota - IDEB (Anos Finais)")
            st.metric("IDEB", dados_escola['IDEB_ANOS_FINAIS'])
            st.caption("A nota do IDEB refere-se aos anos finais do Ensino Fundamental.")

