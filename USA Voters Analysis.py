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

plt.subplot(122)
df.race.value_counts().plot(kind="pie")
plt.title("Distribution of Voters amoung Race")
plt.ylabel("")
plt.show()


# # Visualization 2

# In[24]:


plt.figure(figsize=(12, 4))
plt.subplot(121)
df.educ.value_counts().plot(kind="bar")
plt.title("Distribution of Education")

plt.subplot(122)
df.voter_category.value_counts().plot(kind="bar")
plt.title("Distribution of Voters")
plt.ylabel("")
plt.show()
