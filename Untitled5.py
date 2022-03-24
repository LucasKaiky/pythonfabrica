#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt


# In[22]:


df1 = pd.read_csv('C:\\Users\\Lucas Kaiky\\Desktop\\database\\blaze_pizza_menu.csv')
df1


# In[48]:


from matplotlib.pyplot import figure
figure(figsize = (20, 10), dpi = 80)


# In[47]:


f = df1['food']
p = df1['price']
plt.scatter (f, p, color = 'red', lw=1,)


# In[45]:


df1.sort_values(by = 'price', ascending = True)

