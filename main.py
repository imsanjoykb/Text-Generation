#!/usr/bin/env python
# coding: utf-8

# ### Author : Sanjoy Biswas
# ### Email : sanjoy.eee32@gmail.com
# ### Portfolio : https://imsanjoykb.github.io/

# ### Import Libraries

# In[21]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
import os
import csv
import mysql.connector
from sqlalchemy import create_engine
import pymysql
import pandas as pd


# In[22]:


## Import datafile
df = pd.read_csv(r'E:\AiBeesAsst\AI Bees Project\Data Branch\generatefile.csv', header=None, error_bad_lines = True)
df.head()


# In[23]:


## Checking Null
df.isnull() 


# In[24]:


## Save updated file
df.to_csv('E:\AiBeesAsst\AI Bees Project\Data Branch\generatefileupdated.csv',index=False,header=False)


# ### Connect With Database

# In[25]:


mydb = mysql.connector.connect(host = 'localhost', user = 'root', database = 'textgeneration')
print('Database connected successfully!!')


# In[26]:


cursor = mydb.cursor()
csv_data = csv.reader(open('generatefileupdated.csv'))
for row in csv_data:
    cursor.execute('INSERT INTO textgenerate(comment) VALUES(%s)', row)
    print(row)
    
mydb.commit()
cursor.close()
print('Its Done')


# In[27]:


sqlEngine       = create_engine('mysql+pymysql://root:@127.0.0.1', pool_recycle=3600)
dbConnection    = sqlEngine.connect()
frame           = pd.read_sql("select * from textgeneration.textgenerate", dbConnection);

 
pd.set_option('display.expand_frame_repr', False)
print(frame)
dbConnection.close()


# In[28]:


## Save databasefile
frame.to_csv(r'E:\AiBeesAsst\AI Bees Project\Data Branch\dbfile.csv',index=False)


# In[ ]:




