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


df_region = pd.read_csv("C:/Users/suman/olympics/noc_regions.csv")
df_events = pd.read_csv("C:/Users/suman/olympics/athlete_events.csv")


# In[3]:


df_events.head()


# In[10]:


df_region


# In[6]:


df_region.isnull().count()


# In[9]:


df_region.info()


# In[13]:


df = df_events.merge(df_region,how = 'left', on = "NOC")


# In[14]:


df


# In[15]:


df.rename(columns ={'region' : 'Region', 'notes' : 'Notes'}, inplace = True)
df.head()


# In[16]:


df.describe()


# In[21]:


df.isnull().sum()


# In[23]:


df.query('Team == "India"').head(5)


# In[24]:


df.query('Team == "Japan"').head(5)


# In[34]:


top_ten= df.Team.value_counts().sort_values(ascending=False).head(10)
top_ten


# In[37]:


plt.figure(figsize=(12,5))
plt.xticks(rotation = 45)
plt.title("Overall Participation by Country")
sns.barplot(x=top_ten.index, y = top_ten, palette = 'Set2')


# In[40]:


plt.figure(figsize = (12,6))
plt.title("Age distribution of the Athletes")
plt.xlabel("Age")
plt.ylabel("No. of participants")
plt.hist(df.Age,bins = np.arange(10,80,2),color ='orange', edgecolor ='white');


# In[42]:


winter_sports = df[df.Season == 'Winter'].Sport.unique()
winter_sports


# In[43]:


summer_sports = df[df.Season == 'Summer'].Sport.unique()
summer_sports


# In[51]:


gender_count = df.Sex.value_counts()
men_olympics = df[df.Sex == 'M'].Sex.count()
women_olympics = df[df.Sex == 'F'].Sex.count()
print("Gender count: ", gender_count)
print("Male Participants: ", men_olympics)
print("Female Participants: ", women_olympics)


# In[54]:


plt.figure(figsize =(10,5))
plt.title("Gender distribution")
plt.pie(gender_count, labels=gender_count.index, autopct = '%1.1f%%', startangle = 150, shadow = True)
plt.show()


# In[55]:


df.Medal.value_counts()


# In[60]:


female_participants = df[(df.Sex == 'F') & (df.Season == 'Summer')][['Sex','Year']]
female_participants = female_participants.groupby('Year').count().reset_index()
female_participants.tail()


# In[61]:


women_athlete = df[(df.Sex == 'F') & (df.Season == 'Summer')]


# In[64]:


sns.set(style = 'darkgrid')
plt.figure(figsize =(15,10))
sns.countplot(x = 'Year', data = women_athlete, palette = 'Spectral')
plt.title("Women Partiicipation")
plt.show()


# In[68]:


part = women_athlete.groupby('Year')['Sex'].value_counts()
plt.figure(figsize = (10,5))
part.loc[:,'F'].plot()
plt.title("Plot of Female athelete participation over years", fontsize = 12, fontweight = 'bold')


# In[69]:


gold_medals = df[(df.Medal == 'Gold')]
gold_medals.head()
                 


# In[70]:


gold_medals = gold_medals[np.isfinite(gold_medals['Age'])]


# In[71]:


gold_medals['ID'][gold_medals['Age']>60].count()


# In[73]:


sporting_event = gold_medals['Sport'][gold_medals['Age']>60]
sporting_event


# In[74]:


plt.figure(figsize=(10,5))
plt.tight_layout()
sns.countplot(sporting_event)
plt.title("Gold medals for athletes over 60 years of age")
plt.show()


# In[76]:


gold_medals.Region.value_counts().reset_index(name ='Medal').head()


# In[80]:


total_gold_medals =gold_medals.Region.value_counts().reset_index(name ='Medal').head(7)
g = sns.catplot(x ='index', y = 'Medal', data = total_gold_medals, height = 5, kind ='bar', palette = 'rocket')
g.despine(left=True)
g.set_xlabels("Top 7 Countries")
g.set_ylabels("Number of Medals")
plt.title("Gold Medals per Country")


# In[81]:


max_year = df.Year.max()
max_year


# In[83]:


team_names = df[(df.Year == max_year) & (df.Medal == 'Gold')].Team
team_names.value_counts().head(10)


# In[84]:


sns.barplot(x=team_names.value_counts().head(20), y = team_names.value_counts().head(20).index)
plt.ylabel(None);
plt.xlabel("County wise medal tally in Rio Olympics");


# In[85]:


medal_winners = df[(df['Height'].notnull()) & (df['Weight'].notnull())]


# In[88]:


plt.figure(figsize=(12,10))
axis=sns.scatterplot(x='Height',y = 'Weight', data = medal_winners, hue = 'Sex')
plt.title("Height vs Weight of Olympic medalists")
plt.show()


# In[ ]:




