import numpy as np
import streamlit as st
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier, plot_tree

import seaborn as sns
import pandas as pd
import pickle  
import warnings
warnings.filterwarnings('ignore')

# streamlit run "/Users/joicealves/EBAC_Projeto2/modelo_imp.py"

sns.set(context='talk', style='ticks')

st.set_page_config(
     page_title="Previsão de Renda",
     page_icon="💶",
     layout="wide",
     initial_sidebar_state="expanded",
    )

st.write("## Rodando o modelo")


st.write('A página foi criada como parte de um projeto de análise de renda do'
        ' curso de Ciência de dados da EBAC. Aqui você irá encontrar uma análise '
        'preditiva de renda com base nas variáveis presentes na base de dados')

#lendo o arquivo
renda = pd.read_csv('/Users/joicealves/Downloads/original-2/projeto 2/input/previsao_de_renda.csv')

#trabalhando a base
renda['tempo_emprego']= renda['tempo_emprego'].fillna(renda['tempo_emprego'].mean())

renda['data_ref'] = pd.to_datetime(renda['data_ref'])

# criando a classificação e treinando o modelo

renda["target"] = pd.cut(
    renda["renda"],
    bins=[-np.inf, 3000, 5000, np.inf],
    labels=[0, 1, 2]
)

X = renda.drop(["renda","data_ref","id_cliente", "Unnamed: 0", "target", "sexo"], axis=1)
y = renda["target"] 


X_encoded = pd.get_dummies(X, drop_first=True)

X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.3, random_state=111)

model = DecisionTreeClassifier(max_depth=5, min_samples_leaf=3, random_state=11)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

st.sidebar.header("Insira os dados para previsão:")


user_input = {}
for col in X.columns:
    if X[col].dtype == 'float64' or X[col].dtype == 'int64':
        user_input[col] = st.sidebar.number_input(f"{col}", value=float(X[col].mean()))
    else:
        user_input[col] = st.sidebar.selectbox(f"{col}", renda[col].unique())


input_df = pd.DataFrame([user_input])


input_df = pd.get_dummies(input_df, drop_first=True)

missing_cols = set(X_encoded.columns) - set(input_df.columns)
for col in missing_cols:
    input_df[col] = 0 


input_df = input_df[X_encoded.columns]


if st.sidebar.button("Prever Renda"):
    renda_pred = model.predict(input_df)[0]
    
    
    if renda_pred == 0:
        st.success("Renda Prevista: **Baixa (< R$3.000)**")
        st.write("💳 Limite de crédito: **R$900**")
        st.write("💰 Empréstimo concedido: **R$21.600**")
        st.write("🎖 Classe do cartão: **Standard**")
    elif renda_pred == 1:
        st.success("Renda Prevista: **Média (R$3.000 - R$5.000)**")
        st.write("💳 Limite de crédito: **R$1.500**")
        st.write("💰 Empréstimo concedido: **R$36.000**")
        st.write("🎖 Classe do cartão: **Gold**")
    else:
        st.success("Renda Prevista: **Alta (> R$5.000)**")
        st.write("💳 Limite de crédito: **R$8.500**")
        st.write("💰 Empréstimo concedido: **R$54.000**")
        st.write("🎖 Classe do cartão: **Platinum**")

