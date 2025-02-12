import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st


st.set_page_config(
     page_title="Variáveis numéricas x Renda",
     page_icon="💶",
     layout="wide",
     initial_sidebar_state="expanded",
)

st.title("Variáveis numéricas x Renda")


renda = pd.read_csv('/Users/joicealves/Downloads/original-2/projeto 2/input/previsao_de_renda.csv')

renda['tempo_emprego']= renda['tempo_emprego'].fillna(renda['tempo_emprego'].mean())
renda['data_ref'] = pd.to_datetime(renda['data_ref'])

fig = plt.figure(figsize=(8,8))
renda_numerica = renda.select_dtypes(include=['number'])
renda_corr = renda_numerica.corr()
fig = sns.clustermap(renda_corr, figsize=(10, 10), center=0, cmap="mako")

st.markdown('#### Dadas as diversas variáveis numéricas, iniciaremos com uma matriz de correlação'
            'capturando as variáveis mais relevantes para a renda')

st.pyplot(fig)

st.markdown('Na matriz de correlação, vemos que as variáveis mais relacionadas à renda são'
            ' o tempo de emprego e a posse de veículo. Assim, abaixo segue um gráfico que'
            ' relaciona as 3 variáveis')

fig1 = plt.figure(figsize=(15,15))

fig1 = sns.jointplot(x='tempo_emprego',y='renda',data=renda, hue = "posse_de_veiculo")
st.pyplot(fig1)



