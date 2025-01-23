#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df = pd.read_csv("Universities.csv")
df


# In[3]:


np.mean(df["SAT"])


# In[4]:


np.median(df["SAT"])


# In[5]:


np.var(df["SFRatio"])


# In[6]:


df.describe()


# In[7]:


import matplotlib.pyplot as plt
import seaborn as sns 


# In[8]:


plt.hist(df["GradRate"])


# In[9]:


plt.figure(figsize =(6,3))
plt.title("Graduation Rate")
plt.hist(df["GradRate"])


# In[14]:


s = [20,15,10,25,30,35,28,40,45,60]
scores = pd.Series(s)
scores


# In[15]:


plt.boxplot(scores, vert=False)


# In[17]:


plt.boxplot(scores)


# In[18]:


s = [20,15,10,25,30,35,28,40,45,60,120,150]
scores = pd.Series(s)
scores


# In[19]:


plt.boxplot(scores, vert=False)


# In[20]:


plt.boxplot(scores)


# In[21]:


df = pd.read_csv("Universities.csv")
df


# In[24]:


plt.boxplot(df["SAT"])


# In[27]:


plt.boxplot(df["Top10"])


# In[28]:


plt.boxplot(df["Accept"])


# In[29]:


plt.boxplot(df["SFRatio"])


# In[30]:


plt.boxplot(df["Expenses"])


# In[31]:


plt.boxplot(df["GradRate"])


# In[ ]:




