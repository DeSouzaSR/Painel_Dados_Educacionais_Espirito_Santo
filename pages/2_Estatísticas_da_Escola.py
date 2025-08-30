import streamlit as st

# Configuração da página
st.set_page_config(page_title="Estatísticas", layout="wide")

st.title("📊 Estatísticas das Escolas")
st.markdown("Filtre e selecione uma escola para visualizar seus dados detalhados.")

# --- INÍCIO DO LAYOUT ---
# Dividimos a tela em duas colunas: 1 parte para filtros, 3 para os dados
col_filtro, col_dados = st.columns([1, 3])

# --- CONTAINER DE FILTROS (1/4 da tela) ---
with col_filtro:
    st.header("Filtros")

    # Filtro de Cidade
    cidade = st.selectbox(
        "Selecione a cidade:",
        ["Vitória", "Vila Velha", "Serra", "Cariacica"],
        index=None,
        placeholder="Escolha uma cidade"
    )

    # Filtros de Etapa de Ensino
    st.markdown("**Etapa de Ensino:**")
    ensino_fundamental = st.checkbox("Ensino Fundamental")
    ensino_medio = st.checkbox("Ensino Médio")

    # Filtro/Lista de Escolas
    escola = st.selectbox(
        "Selecione a escola:",
        ["Selecione os filtros acima"],
        disabled=True
    )
    st.caption("Clique em uma escola na lista para ver os detalhes.")
    
    st.write("") # Espaço vertical
    
    # Botão para limpar
    st.button("Limpar Filtros e Seleção", use_container_width=True)

    st.info("Observação: A interatividade dos filtros será implementada na próxima etapa.")


# --- CONTAINER DE DADOS (3/4 da tela) ---
with col_dados:
    # Injetamos o CSS para estilizar o container de dados
    st.markdown("""
    <style>
    .data-container {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 2rem;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .data-container h3 {
        color: #0044ff; /* Cor azul para o nome da escola */
        margin-top: 0;
    }
    </style>
    """, unsafe_allow_html=True)

    # Criamos o container visual usando markdown com a classe CSS
    st.markdown("""
    <div class="data-container">
        <h3>Nome da Escola de Exemplo (Fictício)</h3>
        <p><strong>INEP:</strong> 12345678</p>
        <p><strong>Endereço:</strong> Rua Exemplo, 123, Bairro dos Sonhos, Vitória - ES</p>
        
        <hr> <!-- Linha divisória -->

        <h4>Indicadores de Qualidade</h4>
        
        <!-- Colunas internas para organizar os indicadores -->
    </div>
    """, unsafe_allow_html=True)

    # Para os indicadores, podemos usar st.metric que já tem um bom design
    # E vamos colocá-los dentro de colunas para ficarem lado a lado
    # Acessar o container "invisível" que o Streamlit cria para a coluna `col_dados`
    
    st.write("") # Espaço para alinhar com o conteúdo do markdown acima
    
    metric_cols = st.columns(4)
    with metric_cols[0]:
        st.metric(label="IDEB (Anos Finais)", value="6.5")
    with metric_cols[1]:
        st.metric(label="SAEB (Matemática)", value="280.2")
    with metric_cols[2]:
        st.metric(label="Latitude", value="-20.3155")
    with metric_cols[3]:
        st.metric(label="Longitude", value="-40.3128")

    st.write("")
    st.markdown("<h5>Etapas de Ensino Ofertadas:</h5>", unsafe_allow_html=True)
    
    tag_cols = st.columns(5)
    with tag_cols[0]:
        st.success("✔ Ensino Fundamental")
    with tag_cols[1]:
        st.success("✔ Ensino Médio")
