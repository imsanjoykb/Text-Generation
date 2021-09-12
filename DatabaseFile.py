#!/usr/bin/env python
# coding: utf-8

# In[4]:


import csv
import mysql.connector


# In[9]:


mydb = mysql.connector.connect(host = 'localhost', user = 'root', database = 'textgeneration')
print('Database connected successfully!!')


# In[10]:


cursor = mydb.cursor()
csv_data = csv.reader(open('generatefileupdated.csv'))
for row in csv_data:
    cursor.execute('INSERT INTO textgenerate(comment) VALUES(%s)', row)
    print(row)
    
mydb.commit()
cursor.close()
print('Its Done')


# In[ ]:




