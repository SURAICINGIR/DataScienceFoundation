
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:/Users/Ecem/Desktop/BTS/BTS_MasterInBigData-master/Session_2/3_bike_sharing.csv")
df.head()


# In[3]:


df.info()


# In[5]:


df.shape


# In[6]:


df.isnull().sum()


# In[7]:


df.dtypes


# ###How many avarage rental each season?
# 

# In[10]:


a=df.groupby("season")["count"].mean()
a


# ##Which season have a max rental?

# In[23]:


b=max(a)    #### Merge needed for this questions:) and looking at the manual we see that fall
b


# In[24]:


c=df[["season","b"]].max()


# In[ ]:


df.loc[df.loc[:,"country"]=="Europe"]
df[["name","Age"]].min()

