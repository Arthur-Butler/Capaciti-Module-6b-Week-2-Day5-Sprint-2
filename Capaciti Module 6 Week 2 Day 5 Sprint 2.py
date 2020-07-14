#Importing bar graph utils from pandas
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
import numpy as np
#Importing pandas for dataframe
import pandas as pd
#Importing DataFrame from pandas import
from pandas import DataFrame
#Importing mysql.connector to connect to database
import mysql.connector
#Establishin database connection
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1738art",
    database="sprintdb"
)
#Creatin cursor to navigate database
mycursor=mydb.cursor()
#Fetchin columns from database using SQL
mycursor.execute("SELECT `stock`.`ItemAmount` FROM stock")
ItemAmount=mycursor.fetchall()
#Placing data in lists
y=[]
for row in ItemAmount:
    y.extend(row)
print(y)
mycursor.execute("SELECT `stock`.`Items` FROM stock")
Items=mycursor.fetchall()
x=[]
for row in Items:
    x.extend(row)
print(x)    
y_pos=np.arange(7)
#Diplaying data viually using a bar graph
plt.bar(y_pos, y, align='center', alpha=1)
plt.xticks(y_pos, x)
plt.ylabel('Stock Amount')
plt.xlabel('Item Category')
plt.title('Amount of stock for each item category')
plt.show()
