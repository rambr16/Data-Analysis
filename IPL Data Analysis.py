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


match_data = pd.read_csv("C:/Users/suman/Downloads/ipl/data/IPL Matches 2008-2020.csv")
ball_data = pd.read_csv("C:/Users/suman/Downloads/ipl/data/IPL Ball-by-Ball 2008-2020.csv")


# In[3]:


match_data.head()


# In[4]:


ball_data.head()


# In[8]:



match_data.info()


# In[6]:


ball_data.isnull().sum()


# In[9]:


ball_data.info()


# In[17]:


print("Matches played so far: ", match_data.shape[0])
print("\n Cities played at: ", match_data['city'].unique())
print('\n Teams participated: ', match_data['team1'].unique())


# In[18]:


match_data["Season"] = pd.DatetimeIndex(match_data['date']).year


# In[19]:


match_data.head()


# In[20]:


matches_per_season = match_data.groupby(['Season'])['id'].count().reset_index().rename(columns={'id' : 'matches'})


# In[23]:


matches_per_season


# In[30]:


#visualise matches per season of IPL
sns.countplot(match_data['Season'])
plt.xticks(rotation=45, fontsize=10)
plt.yticks(fontsize =10)
plt.xlabel('Season', fontsize=10)
plt.ylabel("Count", fontsize=10)
plt.title("Matches per season", fontsize = 12, fontweight = "bold")


# In[34]:


season_data = match_data[['id','Season']].merge(ball_data, left_on = 'id', right_on ='id', how = 'left').drop('id', axis = 1)
season_data.head()


# In[38]:


#visualise runs scored in each season

season = season_data.groupby(['Season'])['total_runs'].sum().reset_index()
p = season.set_index('Season')
ax = plt.axes()
ax.set(facecolor = 'white')

sns.lineplot(data = p,palette = "magma")
plt.title("Total runs each season", fontsize = 12, fontweight = 'bold')
plt.show()


# In[42]:


runs_per_season = pd.concat([matches_per_season,season.iloc[:,1]],axis=1)
runs_per_season['Runs per match'] = runs_per_season['total_runs']/runs_per_season['matches']
runs_per_season.set_index('Season', inplace = True)
runs_per_season


# In[44]:


#visualise number of toss won by teams

toss = match_data['toss_winner'].value_counts()
ax = plt.axes()
ax.set(facecolor = 'white')
sns.set(rc={'figure.figsize':(15,10)},style = "darkgrid")
ax.set_title("No. of tosses won by each team", fontsize = 15, fontweight = 'bold')
sns.barplot(y=toss.index, x=toss, orient = 'h',palette = 'icefire', saturation = 1)
plt.xlabel("No. of tosses won")
plt.ylabel("Teams")
plt.show()


# In[47]:


#visualise toss decisions across seasons

ax = plt.axes()
ax.set(facecolor = 'white')
sns.countplot(x = 'Season', hue = 'toss_decision', data= match_data, palette = 'magma', saturation = 1)
plt.xticks(rotation = 45, fontsize = 10)
plt.yticks(fontsize = 10)
plt.xlabel("\n Season", fontsize = 15)
plt.ylabel("Count", fontsize = 15)
plt.title("Toss decisions across season", fontsize = 10, fontweight = 'bold')
plt.show()


# In[48]:


match_data['result'].value_counts()


# In[49]:


match_data.venue[match_data.result != 'runs'].mode()


# In[50]:


match_data.venue[match_data.result != 'wickets'].mode()


# In[53]:


#check which stadium the teams win most after winnign the toss

match_data.venue[match_data.toss_winner == 'Kings XI Punjab'][match_data.winner == 'Kings XI Punjab'].value_counts()


# In[54]:


match_data.venue[match_data.toss_winner == 'Kolkata Knight Riders'][match_data.winner == 'Kolkata Knight Riders'].value_counts()


# In[55]:



match_data.venue[match_data.toss_winner == 'Royal Challengers Bangalore'][match_data.winner == 'Royal Challengers Bangalore'].value_counts()


# In[56]:


match_data.winner[match_data.result != 'runs'].mode()


# In[57]:


match_data.winner[match_data.result != 'wickets'].mode()


# In[58]:


toss = match_data['toss_winner'] == match_data['winner']


# In[61]:


#does toss win matches?
toss = match_data['toss_winner'] == match_data['winner']
plt.figure(figsize = (10,5))
sns.countplot(toss)
plt.show()


# In[62]:


#visualise toss decisions in winning matches

plt.figure(figsize = (12,4))
sns.countplot(match_data.toss_decision[match_data.toss_winner == match_data.winner])
              


# In[67]:


ball_data.head()


# In[68]:


player = (ball_data['batsman'] == 'RT Ponting')
df_ponting = ball_data[player]
df_ponting.head()


# In[70]:


#plot dismissal kinds for Ricky Ponting

df_ponting['dismissal_kind'].value_counts().plot.pie(autopct ='%1.1f%%', shadow = True, rotatelabels = True)
plt.title("Dismissal kind", fontweight = 'bold', fontsize = 10)
plt.show()


# In[71]:


# define a function to return runs by each ball
def count(df_ponting,runs):
    return len(df_ponting[df_ponting['batsman_runs']==runs]) * runs


# In[72]:


#Use above function to print Ricky Pontings run counts

print("Runs scored by Ricky Ponting in 1s : " , count(df_ponting,1))
print("Runs scored by Ricky Ponting in 2s : " , count(df_ponting,2))
print("Runs scored by Ricky Ponting in 3s : " , count(df_ponting,3))
print("Runs scored by Ricky Ponting in 4s : " , count(df_ponting,4))
print("Runs scored by Ricky Ponting in 6s : " , count(df_ponting,6))
                                            


# In[74]:


#Find the match with the highest wining margin
match_data[match_data['result_margin'] == match_data['result_margin'].max()]


# In[82]:


# define variable to store top 10 run scores in IPL

runs = ball_data.groupby(['batsman'])['batsman_runs'].sum().reset_index()
runs.columns=['Batsman' , 'runs']
y = runs.sort_values(by= 'runs', ascending = False).head(10).reset_index().drop('index', axis = 1)
y


# In[87]:


#Visualise top run scores in IPL

ax  = plt.axes()
ax.set(facecolor = 'white')
sns.barplot(x = y['Batsman'],y =y['runs'],palette ='rocket',saturation =1)
plt.xticks(rotation = 80, fontsize = 10)
plt.yticks(fontsize = 10)
plt.xlabel("\n Batsman", fontsize = 10)
plt.ylabel("Runs scores", fontsize = 10)
plt.title("Top 10 run scores in IPL" , fontsize = 15, fontweight = 'bold')


# In[90]:


# Visualise which player got the most number of Player of the Match Titles

ax=plt.axes()
ax.set(facecolor = 'white')
match_data.player_of_match.value_counts()[:10].plot(kind='bar')
plt.xlabel("Player")
plt.ylabel("Count")
plt.title("Most Man of the Match Titles", fontweight = 'bold', fontsize = 12)
plt.show()


# In[ ]:




