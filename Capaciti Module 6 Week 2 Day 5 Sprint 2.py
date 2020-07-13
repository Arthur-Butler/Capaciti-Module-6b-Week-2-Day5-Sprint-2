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
mycursor.execute("SELECT `stock`.`Items`, `stock`.`ItemAmount` FROM stock")
myresult=mycursor.fetchall()
#Placing data in lists
data=[]
for row in myresult:
    data.extend([row])
mycursor.execute("SELECT `stock`.`Items` FROM stock")
Items=mycursor.fetchall()
rows=[]
for row in Items:
    rows.extend(row)
print(data)
df=pd.DataFrame(data,index=rows)
print(df)
#Diplaying data viually using matplotlib
%matplotlib inline
df.plot()
