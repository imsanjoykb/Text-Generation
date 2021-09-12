#!/usr/bin/env python
# coding: utf-8

# ### Import Necessary libraries

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
import os


# In[3]:


## Import datafile
df = pd.read_csv(r'‪E:\AiBeesAsst\AI Bees Project\Data Branch\generatefile.csv', header=None, error_bad_lines = True)
df.head()


# In[4]:


## Checking Null
df.isnull() 


# In[5]:


df.describe()


# In[8]:


## Save updated file
df.to_csv('generatefileupdated.csv',index=False,header=False)

