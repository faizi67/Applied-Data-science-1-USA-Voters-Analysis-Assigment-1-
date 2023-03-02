#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv("nonvoters_data.csv")
df.head()


# # Visualization 1

# In[9]:


plt.figure(figsize=(12, 8))
plt.subplot(121)
df.gender.value_counts().plot(kind="pie")
plt.title("Distribution of Voters amoung Gender")
plt.ylabel("")
