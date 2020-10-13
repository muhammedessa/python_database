#Connecting to Database


import psycopg2


#Connecting to Database

# conn = psycopg2.connect(database="pydatabase", user = "postgres", password = "Muhammed1984", host = "127.0.0.1", port = "5432")
# print("Opened database successfully")


#Create a Table

# conn = psycopg2.connect(database="pydatabase", user = "postgres", password = "Muhammed1984", host = "127.0.0.1", port = "5432")
# print("Opened database successfully")
#
# cur = conn.cursor()
# cur.execute('''CREATE TABLE EMPLOYEES
#       (ID INT PRIMARY KEY     NOT NULL,
#       NAME           TEXT    NOT NULL,
#       AGE            INT     NOT NULL,
#       CITY        CHAR(50),
#       SALARY         REAL);''')
# print("Table created successfully")
#
# conn.commit()
# conn.close()




#INSERT Operation

# conn = psycopg2.connect(database="pydatabase", user = "postgres", password = "Muhammed1984", host = "127.0.0.1", port = "5432")
# print("Opened database successfully")
#
# cur = conn.cursor()
# cur.execute("INSERT INTO EMPLOYEES (ID,NAME,AGE,CITY,SALARY)  VALUES (1, 'Muhammed Essa', 36, 'Kirkuk', 2000.00 )");
# cur.execute("INSERT INTO EMPLOYEES (ID,NAME,AGE,CITY,SALARY)  VALUES (2, 'Ahmed Essa', 33, 'Erbil', 3000.00 )");
# cur.execute("INSERT INTO EMPLOYEES (ID,NAME,AGE,CITY,SALARY)  VALUES (3, 'Osama Essa', 44, 'Mosul', 4000.00 )");
#
# conn.commit()
# print("Records created successfully")
# conn.close()





#SELECT Operation

# conn = psycopg2.connect(database="pydatabase", user = "postgres", password = "Muhammed1984", host = "127.0.0.1", port = "5432")
# print("Opened database successfully")
#
# cur = conn.cursor()
# cur.execute("SELECT id, name, city, salary  from EMPLOYEES")
# rows = cur.fetchall()
# for row in rows:
#    print("ID = ", row[0])
#    print("NAME = ", row[1])
#    print("CITY = ", row[2])
#    print("SALARY = ", row[3], "\n")
#
# print("Operation done successfully")
# conn.close()





#UPDATE Operation

# conn = psycopg2.connect(database="pydatabase", user = "postgres", password = "Muhammed1984", host = "127.0.0.1", port = "5432")
# print("Opened database successfully")
#
# cur = conn.cursor()
# cur.execute("UPDATE EMPLOYEES set SALARY = 25000.00 where ID = 1")
# conn.commit()
# print("Total number of rows updated :", cur.rowcount)
#
# cur.execute("SELECT id, name, city, salary  from EMPLOYEES")
# rows = cur.fetchall()
# for row in rows:
#    print("ID = ", row[0])
#    print("NAME = ", row[1])
#    print("CITY = ", row[2])
#    print("SALARY = ", row[3], "\n")
#
# print("Operation done successfully")
# conn.close()







#DELETE Operation

# conn = psycopg2.connect(database="pydatabase", user = "postgres", password = "Muhammed1984", host = "127.0.0.1", port = "5432")
# print("Opened database successfully")
#
# cur = conn.cursor()
# cur.execute("DELETE from EMPLOYEES where ID=2;")
# conn.commit()
# print("Total number of rows deleted :", cur.rowcount)
#
# cur.execute("SELECT id, name, city, salary  from EMPLOYEES")
# rows = cur.fetchall()
# for row in rows:
#    print("ID = ", row[0])
#    print("NAME = ", row[1])
#    print("CITY = ", row[2])
#    print("SALARY = ", row[3], "\n")
#
# print("Operation done successfully")
# conn.close()











