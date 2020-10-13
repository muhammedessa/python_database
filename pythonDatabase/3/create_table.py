#Creating a Table
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="muhammed",
  password="muhammed",
  database="mydatastores"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE employees (name VARCHAR(255), age VARCHAR(255), province VARCHAR(255))")

mydb.close()







#Check if Table Exists

# import mysql.connector
#
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="muhammed",
#   password="muhammed",
#   database="mydatastore"
# )
#
# mycursor = mydb.cursor()
#
# mycursor.execute("SHOW TABLES")
#
# for x in mycursor:
#   print(x)









#Primary Key

# import mysql.connector
#
# mydb = mysql.connector.connect(
#       host="localhost",
#       user="muhammed",
#       password="muhammed",
#       database="mydatastore"
# )
#
# mycursor = mydb.cursor()
#
# mycursor.execute("CREATE TABLE students (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age VARCHAR(255))")








import mysql.connector

# mydb = mysql.connector.connect(
#       host="localhost",
#       user="muhammed",
#       password="muhammed",
#       database="mydatastore"
# )
#
# mycursor = mydb.cursor()
#
# mycursor.execute("ALTER TABLE employees ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")


















