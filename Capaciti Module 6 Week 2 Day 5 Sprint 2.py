#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
from pandas import DataFrame
df=pd.read_csv("Sprint2.csv")
df.head()


# In[ ]:


db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )

# prepare a cursor object using cursor() method

cursor = db.cursor()

# Drop table if it already exist using execute() method.

cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# Create table as per requirement

sql = """CREATE TABLE EMPLOYEE (

         FIRST_NAME  CHAR(20) NOT NULL,

         LAST_NAME  CHAR(20),

         AGE INT,  

         SEX CHAR(1),

         INCOME FLOAT )"""

cursor.execute(sql)

# disconnect from server

db.close()

import pandas as pd
from pandas import DataFrame
df=pd.read_csv("Sprint2.csv")
df.head()
df.count(axis='index')
#df["Chips"].value_counts()
#%matplotlib inline
#df.plot()