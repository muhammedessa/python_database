import os
import time
import socket
import datetime
import mysql.connector

hostname = "google.com"
response = os.system("ping -c 1 " + hostname)

def database_updates(ip , networkdate):
    mydb = mysql.connector.connect(
        host="localhost",
        user="muhammed",
        password="muhammed",
        database="networkdb"
    )
    mycursor = mydb.cursor()
    sql = "INSERT INTO networkstatus (ip, time) VALUES (%s,%s )"
    val = (ip, networkdate)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

    mydb.close()



def check_network(host, res):

    ip = socket.gethostbyname(host)
    now = datetime.datetime.now()

    if res == 0:
      print(hostname, 'is up!', 'Google ip is : ', ip , ' time: ' ,now.strftime("%Y-%m-%d %H:%M:%S"))
      database_updates(ip, now.strftime("%Y-%m-%d %H:%M:%S"))
    else:
      print(host, 'is down!', ip)
    time.sleep(3)

if __name__ == '__main__':
    while True:
        check_network(hostname, response)












#create Database

# import mysql.connector
#
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="muhammed",
#   password="muhammed"
# )
# mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE networkdb")
# mydb.close()



#create table

# import mysql.connector
#
# mydb = mysql.connector.connect(
#       host="localhost",
#       user="muhammed",
#       password="muhammed",
#       database="networkdb"
# )
# mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE networkstatus (id INT AUTO_INCREMENT PRIMARY KEY, ip VARCHAR(255), time VARCHAR(255))")
# mydb.close()








