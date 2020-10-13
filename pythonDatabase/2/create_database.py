#create a database named "mydatastore"

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="muhammed",
  password="muhammed"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatastores")

mydb.close()




#Check if Database Exists

# import mysql.connector
#
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="muhammed",
#   password="muhammed"
# )
#
# mycursor = mydb.cursor()
#
# mycursor.execute("SHOW DATABASES")
#
# for x in mycursor:
#   print(x)




#Try connecting to the database "mydatastore"

# import mysql.connector
#
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="muhammed",
#   password="muhammed",
#   database="mydatastore"
# )