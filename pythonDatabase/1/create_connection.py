#pip install mysql-connector-python



#Create Connection
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="muhammed",
  password="muhammed"
)

print(mydb)

mydb.close()

