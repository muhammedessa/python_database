import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="muhammed",
    password="muhammed",
    database="mydatastore"
)

mycursor = mydb.cursor()

sql = "DELETE FROM employees WHERE id = %s"
myid = ("2", )

mycursor.execute(sql, myid)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")