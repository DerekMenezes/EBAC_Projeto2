import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# streamlit run "/Users/joicealves/Downloads/original-2/projeto 2/projeto_2.py"

sns.set(context='talk', style='ticks')

st.set_page_config(
     page_title="Previsão de Renda",
     page_icon="💶",
     layout="wide",
     initial_sidebar_state="expanded",
)

st.write('# Análise exploratória da previsão de renda')
st.write('### Navegue pelo menu para ver a análise das variáveis categóricas e numéricas')

renda = pd.read_csv('/Users/joicealves/Downloads/original-2/projeto 2/input/previsao_de_renda.csv')

#plots
fig, ax = plt.subplots(7,1,figsize=(10,70))
renda[['posse_de_imovel','renda']].plot(kind='hist', ax=ax[0])
sns.lineplot(x='data_ref',y='renda', hue='posse_de_veiculo',data=renda, ax=ax[1])
ax[1].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref',y='renda', hue='qtd_filhos',data=renda, ax=ax[2])
ax[2].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref',y='renda', hue='tipo_renda',data=renda, ax=ax[3])
ax[3].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref',y='renda', hue='educacao',data=renda, ax=ax[4])
ax[4].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref',y='renda', hue='estado_civil',data=renda, ax=ax[5])
ax[5].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref',y='renda', hue='tipo_residencia',data=renda, ax=ax[6])
ax[6].tick_params(axis='x', rotation=45)

sns.despine()
st.pyplot(plt)

st.write('## Variáveis categóras x Renda')
st.write('## Análise bivariada')
fig, ax = plt.subplots(7,1,figsize=(15,90))
sns.barplot(x='posse_de_imovel',y='renda',data=renda, ax=ax[0])
sns.barplot(x='posse_de_veiculo',y='renda',data=renda, ax=ax[1])
sns.barplot(x='qtd_filhos',y='renda',data=renda, ax=ax[2])
sns.barplot(x='tipo_renda',y='renda',data=renda, ax=ax[3])
ax[3].tick_params(axis='x', rotation=45)
sns.barplot(x='educacao',y='renda',data=renda, ax=ax[4])
ax[4].tick_params(axis='x', rotation=45)
sns.barplot(x='estado_civil',y='renda',data=renda, ax=ax[5])
ax[5].tick_params(axis='x', rotation=45)
sns.barplot(x='tipo_residencia',y='renda',data=renda, ax=ax[6])
ax[6].tick_params(axis='x', rotation=45)
sns.despine()
st.pyplot(plt)



st.write("## Variáveis numéricas x Renda")
renda['tempo_emprego']= renda['tempo_emprego'].fillna(renda['tempo_emprego'].mean())
renda['data_ref'] = pd.to_datetime(renda['data_ref'])

fig = plt.figure(figsize=(8,8))
renda_numerica = renda.select_dtypes(include=['number'])
renda_corr = renda_numerica.corr()
fig = sns.clustermap(renda_corr, figsize=(10, 10), center=0, cmap="mako")

st.pyplot(fig)

fig1 = plt.figure(figsize=(15,15))

fig1 = sns.jointplot(x='tempo_emprego',y='renda',data=renda, hue = "posse_de_veiculo")
st.pyplot(fig1)




