#Insert Into Table

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="muhammed",
  password="muhammed",
  database="mydatastore"
)

mycursor = mydb.cursor()
sql = "INSERT INTO employees (name, age, province) VALUES (%s,%s, %s)"
val = ("Muhammed Essa", "36", "Kirkuk")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")

mydb.close()





#Insert Multiple Rows

# import mysql.connector
#
# mydb = mysql.connector.connect(
#           host="localhost",
#           user="muhammed",
#           password="muhammed",
#           database="mydatastore"
# )
#
# mycursor = mydb.cursor()
#
# sql = "INSERT INTO employees (name, age, province) VALUES (%s,%s, %s)"
# val = [
#   ("Muhammed Essa", "36", "Kirkuk"),
#   ("Ahmed Essa", "30", "Baghdad"),
#   ("Osama Essa", "39", "Mosul"),
#   ("Ali Essa", "42", "Erbil")
# ]
#
# mycursor.executemany(sql, val)
#
# mydb.commit()
#
# print(mycursor.rowcount, "was inserted.")






# return the ID

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
# sql = "INSERT INTO employees (name, age, province) VALUES (%s,%s, %s)"
# val = ("Muhammed Essa", "36", "Kirkuk")
#
# mycursor.execute(sql, val)
#
# mydb.commit()
#
# print("1 record inserted, ID:", mycursor.lastrowid)




















