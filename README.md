# Projeto: Painel de Dados Educacionais do Espírito Santo

Projeto didático para disciplina de **Cloud Computing para produtos de dados** do curso de Pós-graduação em Mineração de Dados do IFES - SERRA - ES. O projeto consiste numa aplicação web, usando [Streamlit](https://streamlit.io/), no qual faremos um MVP que será testado pelos colegas de sala e analisado pelo professor.

- Professor: _Maxwell Monteiro_ 
- Aluno: _Sandro Ricardo De Souza_

### Link para o projeto publicado
https://paineldadoseducacionaisespiritosanto-awc2zdfsj4srjzag6ydtkz.streamlit.app/

## 1. Definição do Tema e Objetivos:

O objetivo é fornecer uma plataforma interativa para a visualização de dados educacionais das escolas do estado do Espírito Santo. A aplicação será estruturada em quatro seções principais: (i) Apresentação do projeto; (ii) Mapa interativo com a geolocalização das escolas; (iii) Consulta de estatísticas e características das instituições; e (iv) Visualização de indicadores de qualidade como o IDEB e SAEB.

## 2. Escolha e Planejamento dos Dados:

As fontes de dados primárias para este projeto são os microdados públicos disponibilizados pelo Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP). Os seguintes conjuntos de dados foram selecionados:

Microdados do Censo Escolar (Edição mais recente): Utilizado para extrair informações cadastrais das escolas, como nome, código INEP, localização (município e endereço para geocodificação), dependência administrativa (municipal, estadual, particular) e etapas de ensino ofertadas. Os dados serão pré-processados para filtrar apenas as escolas do estado do Espírito Santo (código UF 32).

Resultados do Ideb por Escola (Edição mais recente): Utilizado para obter os indicadores de qualidade de cada instituição, que serão posteriormente vinculados aos dados do Censo Escolar através do código INEP da escola.

## 3. Estrutura Tecnológica:

A aplicação será desenvolvida em Python utilizando a biblioteca Streamlit. O controle de versão e o código-fonte serão gerenciados em um repositório no GitHub, e o deploy online da aplicação será feito através do Streamlit Community Cloud.

## 4. Estrutura de arquivos

```
/
├── .streamlit/
│   └── config.toml
├── data/
│   └── amostra_escolas.csv
├── pages/
│   ├── 1_Mapa_Interativo.py
│   ├── 2_Estatisticas_da_Escola.py
│   └── 3_Indicadores_de_Qualidade.py
├── Apresentação.py
└── README.md
```

## 5. Avaliação:

Construção em 5 etapas de um MVP baseado em dados

- [x] Etapa 1 - 10%: Esboço (definição de tema e escolha de dados);
- [x] Etapa 2 - 20%: Versão de baixa Estética e usabilidade Sem os dados;
- [x] Etapa 3 - 20%: Versão de baixa Estética e usabilidade Com os dados;
- [ ] Etapa 4 - 20%: Validação com usuários (outros alunos);
- [ ] Etapa 5 - 30%: Finalização do MVP.

