import streamlit as st
import pandas as pd
import seaborn as sns

# streamlit run "/Users/joicealves/EBAC_Projeto2/Home Page.py"

sns.set(context='talk', style='ticks')

st.set_page_config(
     page_title="Previsão de Renda",
     page_icon="💶",
     layout="wide",
     initial_sidebar_state="expanded",
)

st.write('# Análise exploratória e preditiva da renda')

st.write('A página foi criada como parte de um projeto de análise de renda do'
        ' curso de Ciência de dados da EBAC. Aqui você irá encontrar a análise '
        'descritiva das variáveis presentes na base de dados '
        'além de um modelo de Machine Learning que prevê a renda de um indivíduo com '
        'base em suas informações de cadastro')





st.write('#### Navegue pelo menu para ver a análise das variáveis categóricas e numéricas')

renda = pd.read_csv('/Users/joicealves/Downloads/original-2/projeto 2/input/previsao_de_renda.csv')


st.write('Cálculo do Valor de Empréstimo: O valor total do empréstimo é estimado com base na renda prevista, '
         'seguindo a premissa de que as parcelas mensais não devem exceder 30% da renda mensal do cliente. '
         'Considerando um prazo de pagamento de 24 meses, o montante é calculado da seguinte forma:')

st.write('VALOR DO EMPRÉSTIMO = 24 × (0.3 × Renda Prevista)')

st.write('Tabela: premissas para o resultado do modelo')

df = pd.DataFrame(
    {
        "Nível de Renda": ["Até 3K", "De 3K até R$ 5K","Acima dos 5K"],
        "Limite de Crédito": ["900 Reais", "1.500 Reais","R$8.500 Reais"],
        "Empréstimo Concedido": ["21.600 Reais", "36.000 Reais","54.000 Reais"],
        "Classe do Cartão": ["Standard", "Gold","Platinum"],
    }
)
st.table(df)

