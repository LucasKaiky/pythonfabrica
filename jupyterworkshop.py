#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[4]:


df1 = pd.read_csv('C:\\Users\\Lucas Kaiky\\Downloads\\dados_planetas.txt')

df1


# In[11]:


from matplotlib.pyplot import figure
figure(figsize = (15, 6), dpi = 80)


# In[17]:


p = df1['planet'] #atribuição de variável com colchetes

t = df1['mean_temperature']

plt.plot (p, t, color = 'red', lw = 8) #lw linha do plot


# In[20]:


df1.sort_values(by = 'mass', ascending = True)
#dataframe ascendendo, organiza o df
#False deixa decrescente

