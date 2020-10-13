# import mysql.connector
#
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="muhammed",
#     password="muhammed",
#     database="mydatastore"
# )
#
# mycursor = mydb.cursor()
# mycursor.execute("SELECT * FROM employees")
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)
#
# mydb.close()











# import mysql.connector
#
# mydb = mysql.connector.connect(
#         host="localhost",
#         user="muhammed",
#         password="muhammed",
#         database="mydatastore"
# )
#
# mycursor = mydb.cursor()
# mycursor.execute("SELECT * FROM employees")
# myresult = mycursor.fetchone()
#
# print(myresult)
#
# mydb.close()







#ORDER BY DESC

# import mysql.connector
#
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="muhammed",
#     password="muhammed",
#     database="mydatastore"
# )
#
# mycursor = mydb.cursor()
#
# sql = "SELECT * FROM employees ORDER BY name DESC"
#
# mycursor.execute(sql)
#
# myresult = mycursor.fetchall()
#
# for x in myresult:
#   print(x)






