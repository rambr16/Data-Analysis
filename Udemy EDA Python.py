#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from plotly.subplots import make_subplots
from datetime import datetime


# In[2]:


df_udemy = pd.read_csv("C:/Users/suman/Downloads/udemy.csv")


# In[3]:


df_udemy.head()


# In[4]:


df_udemy['subject'].unique()


# In[8]:


df_udemy['subject'].value_counts()


# In[7]:


df_udemy['subject'].value_counts().plot()


# In[26]:


df_udemy[df_udemy.is_paid== False]


# In[27]:


df_udemy[df_udemy.is_paid== True]


# In[30]:


df_udemy.sort_values('num_subscribers', ascending = False).head(10)


# In[31]:


df_udemy.sort_values('num_subscribers', ascending = True).head(15)


# In[44]:


df_udemy[(df_udemy.subject == 'Graphic Design') & (df_udemy.price == '100')]


# In[45]:


df_udemy[df_udemy.course_title.str.contains('Python')]


# In[56]:



df_udemy.dtypes
df_udemy['published_timestamp']=pd.to_datetime(df_udemy.published_timestamp)
df_udemy.dtypes
df_udemy['Year'] = df_udemy['published_timestamp'].dt.year
df_udemy[df_udemy.Year ==2015]


# In[61]:


df_udemy.groupby('level')['num_subscribers'].max()


# In[62]:


df_udemy.groupby('level').max()


# In[ ]:




