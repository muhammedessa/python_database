import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="muhammed",
    password="muhammed",
    database="mydatastore"
)

mycursor = mydb.cursor()

sql = "UPDATE employees SET age = %s WHERE id = %s"
val = ("44", "3")

mycursor.execute(sql, val)
mydb.commit()

print(mycursor.rowcount, "record(s) affected")