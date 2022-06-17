#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import libraries

get_ipython().system('pip install bar_chart_race')

import bar_chart_race as bcr
import pandas as pd
import seaborn as sns
import numpy as np

import matplotlib
from matplotlib.animation import FuncAnimation as ani
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from matplotlib.pyplot import figure

get_ipython().run_line_magic('matplotlib', 'inline')
matplotlib.rcParams['figure.figsize'] = (12,8) # Adjusts the configuration of the plots we will create


# In[2]:


# file uploaded for data analysis
    
df=pd.read_csv("movies.csv", index_col=None, na_values=['NA']) # file uploaded for data analysis


# In[3]:


# preview top 7 rows of data

df.head(7)


# In[4]:


#preview bottom 7 rows of data

df.tail(7)


# In[5]:


# dropping all null values in dataset

df.dropna()


# In[11]:


# change datatype of columns
# used the drop.na method to remove NA values

df = df.dropna()
df = df.astype({'budget':'int'})
df = df.astype({'gross':'int'})
df = df.astype({'votes':'int'})
df = df.astype({'runtime':'int'})


# In[29]:


# Locating all movies starring Denzel Washington

df.loc[(df['star'] == 'Denzel Washington')]


# In[18]:


# creating a budget/gross correlation with a scatterplot through seaborn

# plotting the data and altering the color

sns.set_style('darkgrid')
sns.regplot(x='budget',y='gross', data=df, scatter_kws={'color':'orange'}, line_kws={'color':'blue'})

plt.title('Budget vs. Gross')
plt.xlabel('Budget')
plt.ylabel('Gross')
plt.show()


# In[13]:


# finding the correlations in the dataset
# budget/gross has the highest correlation

df.corr(method='pearson') #3 types of methods, pearson, kendall, spearman. using default method(pearson)


# In[14]:


# now that we have the correlation data, let's visualize it
# correlation matrix shows high correlation between budget & gross

sns.heatmap(df.corr(), annot=True)
plt.show()

