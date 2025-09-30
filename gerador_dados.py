import pandas as pd
import numpy as np

def gerar_dados_escolas(num_escolas_por_cidade=5):
    """
    Gera um DataFrame com dados fictícios de escolas da Região Metropolitana
    do Espírito Santo e o salva como um arquivo CSV.

    Args:
        num_escolas_por_cidade (int): O número de escolas a serem geradas para cada cidade.
    """
    # Dicionário com as cidades e suas coordenadas centrais aproximadas
    cidades = {
        "Vitória": {"lat": -20.2976, "lon": -40.2958},
        "Vila Velha": {"lat": -20.3378, "lon": -40.2942},
        "Serra": {"lat": -20.1281, "lon": -40.3082},
        "Cariacica": {"lat": -20.2642, "lon": -40.4205}
    }
    
    # Listas para gerar nomes de escolas mais realistas
    prefixos = ["EMEF", "EEEFM", "CEEFTI", "Colégio", "Escola"]
    nomes_meio = ["Presidente", "Professor", "Pastor", "São", "Nossa Senhora"]
    sufixos = ["Getúlio Vargas", "Anísio Teixeira", "José de Anchieta", "da Penha", "das Graças", "do Brasil"]

    lista_escolas = []
    codigo_inep_inicial = 32010000

    print("Iniciando a geração de dados...")

    for cidade, coords in cidades.items():
        for i in range(num_escolas_por_cidade):
            # Gera um nome de escola combinando partes aleatórias
            nome_escola = f"{np.random.choice(prefixos)} {np.random.choice(nomes_meio)} {np.random.choice(sufixos)}"
            
            # Garante que não haja nomes duplicados na mesma cidade
            nome_escola = f"{nome_escola} {i+1}"
            
            # Gera coordenadas com uma pequena variação aleatória em torno do centro da cidade
            lat = coords["lat"] + np.random.normal(0, 0.035)
            lon = coords["lon"] + np.random.normal(0, 0.035)

            # Define as etapas de ensino (garantindo que pelo menos uma seja ofertada)
            ens_fundamental = np.random.choice([0, 1])
            ens_medio = np.random.choice([0, 1])
            if ens_fundamental == 0 and ens_medio == 0:
                ens_fundamental = 1

            # Gera as notas dentro de um intervalo realista
            ideb = round(np.random.uniform(4.5, 7.2), 1)
            saeb_mt = round(np.random.uniform(250.0, 330.0), 1)
            saeb_lp = round(np.random.uniform(240.0, 320.0), 1)

            # Define a rede de ensino com pesos diferentes
            rede = np.random.choice(["Estadual", "Municipal", "Privada"], p=[0.3, 0.6, 0.1])

            # Adiciona os dados da escola à lista
            lista_escolas.append({
                "NO_ENTIDADE": nome_escola,
                "CO_ENTIDADE": codigo_inep_inicial,
                "NO_MUNICIPIO": cidade,
                "IN_FUNDAMENTAL": ens_fundamental,
                "IN_MEDIO": ens_medio,
                "IDEB_ANOS_FINAIS": ideb,
                "MEDIA_SAEB_MT": saeb_mt,
                "MEDIA_SAEB_LP": saeb_lp,
                "LATITUDE": lat,
                "LONGITUDE": lon,
                "TP_DEPENDENCIA": rede,
                "DS_ENDERECO": f"Rua Fictícia {i+1}, Bairro Exemplo, {cidade}"
            })
            
            codigo_inep_inicial += 1

    # Converte a lista de dicionários em um DataFrame do pandas
    df_escolas = pd.DataFrame(lista_escolas)
    
    # Define o nome do arquivo de saída
    nome_arquivo = "dados_escolas_es.csv"

    # Salva o DataFrame em um arquivo CSV, sem o índice
    df_escolas.to_csv("data/" + nome_arquivo, index=False, sep=';', decimal=',')
    
    print("-" * 50)
    print(f"Arquivo '{nome_arquivo}' gerado com sucesso!")
    print(f"Total de escolas criadas: {len(df_escolas)}")
    print(f"Cidades incluídas: {list(cidades.keys())}")
    print("Visualização das 5 primeiras linhas:")
    print(df_escolas.head())
    print("-" * 50)

# Bloco principal para executar a função quando o script for chamado
if __name__ == "__main__":
    gerar_dados_escolas(num_escolas_por_cidade=5)
