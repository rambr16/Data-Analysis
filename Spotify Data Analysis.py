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


df_tracks = pd.read_csv("C:/Users/suman/Desktop/spotify/tracks.csv")


# In[3]:


df_tracks.head()


# In[4]:


pd.isnull(df_tracks).sum()


# In[5]:


df_tracks.info()


# In[6]:


sorted_df = df_tracks.sort_values("popularity",ascending = True).head(10)


# In[7]:


sorted_df


# In[8]:


most_popular = df_tracks.query('popularity>90', inplace = False).sort_values('popularity', ascending = False)
most_popular[:10]


# In[9]:


df_tracks.set_index("release_date", inplace = True)
df_tracks.index=pd.to_datetime(df_tracks.index)
df_tracks.head()


# In[10]:


df_tracks["duration"] = df_tracks["duration_ms"].apply(lambda x: round(x/1000))
df_tracks.drop("duration_ms", inplace = True, axis = 1)
df_tracks.head()


# In[20]:


corr_df = df_tracks.drop(["key","mode","explicit"],axis =1).corr(method='pearson')
plt.figure(figsize=(14,6))
heatmap = sns.heatmap(corr_df,annot = True,fmt=".1g",vmin = -1, vmax = 1,center = 0, cmap ="inferno",linewidths=1,linecolor = 'Black')
heatmap.set_title("Correalation Heat Map")
heatmap.set_xticklabels(heatmap.get_xticklabels(),rotation = 90)


# In[21]:


sample_df = df_tracks.sample(int(0.004*len(df_tracks)))


# In[22]:


print(len(sample_df))


# In[23]:


plt.figure(figsize =(10,6))
sns.regplot(data = sample_df, y = "loudness", x ="energy", color = "c").set(title = "Loudness Vs Energy")


# In[25]:


plt.figure(figsize =(10,6))
sns.regplot(data = sample_df, y = "popularity", x ="acousticness", color = "b").set(title = "Popularity Vs Acousticness")


# In[27]:


df_tracks['dates'] = df_tracks.index.get_level_values('release_date')
df_tracks.dates = pd.to_datetime(df_tracks.dates)
years = df_tracks.dates.dt.year


# In[29]:


sns.displot(years,discrete = True,aspect = 2,height = 5,kind = 'hist').set(title = "Number of songs per year")


# In[31]:


total_duration = df_tracks.duration
fig_dims = (18,7)
fig, ax = plt.subplots(figsize = fig_dims)
fig = sns.barplot(x = years, y = total_duration, ax = ax, errwidth = False).set(title = "Year vs duration of songs")
plt.axticks(rotate = 90)


# In[37]:


total_duration = df_tracks.duration
sns.set_style(style = "whitegrid")
fig_dims = (18,7)
fig, ax = plt.subplots(figsize = fig_dims)
fig = sns.lineplot(x = years, y = total_duration, ax = ax).set(title = "Year vs duration of songs")
plt.xticks(rotation= 60)


# In[38]:


df_genre = pd.read_csv("C:/Users/suman/Desktop/spotify/SpotifyFeatures.csv")


# In[39]:


df_genre.head()


# In[41]:


plt.title("Duration of songs in different genres")
sns.color_palette("rocket", as_cmap = True)
sns.barplot(y= 'genre', x = 'duration_ms',data=df_genre )
plt.xlabel("Duration in ms")
plt.ylabel("Genre")


# In[47]:


sns.set_style(style = "darkgrid")
plt.figure(figsize=(10,5))
famous = df_genre.sort_values("popularity", ascending = False).head(10)
sns.barplot(y = "genre", x ="popularity", data = famous).set(title =" Top 5 Genres ")


# In[ ]:




