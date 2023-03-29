#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np
import seaborn as sns


# In[2]:


# reading the file
df = pd.read_csv('bank.csv')


# In[3]:


df.head()


# In[4]:


df.info()


# In[5]:


df.describe()


# In[6]:


df.isnull().sum()


# In[7]:


df.shape


# In[8]:


# checking how many total variables are there in the target variable or target feature
df['month'].value_counts()


# In[9]:


# Finding out the mean, median and minimum value of the pdays column

print(df['pdays'].mean()) 
print(df['pdays'].median())
print(df['pdays'].min())


# In[14]:


df['pdays'].value_counts()


# In[17]:


plt.boxplot(df['pdays'])


# In[18]:


df.groupby(df['education'])['balance'].median().plot.barh()


# In[19]:


# here getting all the categorical and numerical features in a seperate list

obj_col = []
num_col = []
for i in newdf.columns:
    if df[i].dtype=='O':
        obj_col.append(i)
    else:
        num_col.append(i)


# In[20]:


print("Categorical Columns: ",obj_col)
print("Numerical Columns: ",num_col)


# In[21]:


# checking the correlation between the independent and dependent feature
plt.figure(figsize=(15,10))
sns.heatmap(df.corr(), annot=True)
plt.title('Correlation between all the Numerical Features')


# In[ ]:




