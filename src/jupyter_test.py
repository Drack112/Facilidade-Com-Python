#!/usr/bin/env python
# coding: utf-8

# # Jupyter Teste

#  ## Esse arquivo tem apenas funções de ser um Playground com o Jupyter e tirar algumas conclusões sobre o mesmo.
#  
#  ### Um pouco de pandas será incluido também :)

# ### Teste de Loop

# In[7]:


list = [1,2,3,4,5]

for c in list:
    print(list)


# ### Teste de Dados com Pandas e Numpy

# In[14]:


import pandas as pd
import numpy as np

# creating data
dataNP = np.array([[1,4], [2,5], [4,6]])
dataNP


# ### Criação de Dataframes com Pandas

# In[28]:


# Criando Dataframe
print(pd.DataFrame(dataNP))

# Dataframe com params
df = pd.DataFrame(dataNP, index=["Row1", "Row2", "Row3"], 
                 columns=["col1", "col2"])
      
df


# ### Teste com listas

# In[29]:


states = ["São Paulo", "Rio De Janeiro", "Minas Gerais"]
population = [12341, 412424, 51251]

# criar tabelinha easy
dict_states = {
    'States': states,
    'Population': population
}

df_dict = pd.DataFrame(dict_states)
df_dict


# ### Teste com um arquivo CSV

# In[48]:


csvPD = pd.read_csv("/home/drack/example.csv", encoding='UTF-8')

csvPD


# In[52]:


csvPD.head(10)


# In[53]:


csvPD.tail(10)


# ### Definindo certas propriedades com o Pandas

# In[54]:


# pegar informações de linhas e de colunas
csvPD.shape


# In[85]:


pd.set_option('display.max_rows', 10)
csvPD


# ### Atributos

# In[68]:


# Pegar o index do arquivo
csvPD.index


# In[70]:


# Exibir colunas
csvPD.columns


# In[71]:


# DTypes -> os tipos de dados de cada coluna
csvPD.dtypes


# In[72]:


# Info 
csvPD.info()


# # Descibre
# csvPD.describe()

# ### Funções

# In[74]:


len(csvPD)


# In[75]:


max(csvPD.index)


# In[76]:


min(csvPD.index)


# In[77]:


type(csvPD)


# In[79]:


round(csvPD, 2)


# ### Sintaxé

# In[88]:


csv_pd = pd.read_csv("/home/drack/example.csv", encoding='UTF-8')

csv_pd


# In[86]:


csv_pd["Casos por dia"]


# In[87]:


type(csv_pd["Óbitos por dia"])


# In[94]:


# Selecionando Colunas
csv_pd[["Casos por dia", "Óbitos por dia"]]


# ### Operações em Colunas

# In[96]:


csv_pd['Casos por dia'].sum()


# In[99]:


csv_pd['Casos por dia'].count()


# In[100]:


csv_pd['Casos por dia'].mean()


# In[101]:


csv_pd['Casos por dia'].std()


# In[102]:


csv_pd['Casos por dia'].max()


# In[103]:


csv_pd['Casos por dia'].min()


# In[105]:


# mesma coisa
csv_pd.describe()


# ### Operações em Linhas

# In[106]:


csv_pd["Casos por dia"] + csv_pd["Óbitos por dia"]


# In[107]:


csv_pd_row= (csv_pd["Casos por dia"] + csv_pd["Óbitos por dia"])
csv_pd_row


# ### Valores de contagem

# In[108]:


len(csv_pd['Casos por dia'])


# In[109]:


csv_pd['Casos por dia'].count()


# In[111]:


csv_pd['Casos por dia'].value_counts()
csv_pd['Casos por dia'].value_counts(normalize=True)


# ### Sort

# In[114]:


csv_pd.sort_values('Casos por dia')


# In[115]:


csv_pd.sort_values('Casos por dia', ascending=False)


# In[121]:


csv_pd.sort_values(['Casos por dia', 'Óbitos por dia'], ascending=False)


# ### Pivot

# In[126]:


csv_pd.pivot(index="Data", columns="Casos por dia")


# ### Plots

# In[136]:


csv_p = pd.read_csv("/home/drack/population_total.csv", encoding="UTF-8")

csv_p.plot(kind='line',
          title="População 1955-2020")


# In[ ]:


csv_p.plot(kind='bar')


# In[ ]:


csv_p.plot(kind='pie', title="População 1955-2020")


# In[ ]:




