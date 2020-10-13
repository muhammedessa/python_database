import os
import time
import socket
import datetime
import psycopg2

hostname = "google.com"
response = os.system("ping -c 1 " + hostname)

def database_updates(ip , networkdate):
    conn = psycopg2.connect(database="networkdata", user = "postgres", password = "Muhammed1984", host = "127.0.0.1", port = "5432")
    cur = conn.cursor()
    sql_data = "INSERT INTO networkstatus (IP, MYDATE )  VALUES (%s,%s)"
    record_to_insert = (ip, networkdate )
    cur.execute(sql_data, record_to_insert)
    conn.commit()
    print("Records created successfully")
    conn.close()


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














#Connecting to Database and create table

# import psycopg2
# conn = psycopg2.connect(database="networkdata", user = "postgres", password = "Muhammed1984", host = "127.0.0.1", port = "5432")
# print("Opened database successfully")
#
# cur = conn.cursor()
# cur.execute('''CREATE TABLE NETWORKSTATUS
#       (ID INT PRIMARY KEY     NOT NULL,
#       IP           TEXT    NOT NULL,
#       MYDATE       TEXT     NOT NULL
#       );''')
# print("Table created successfully")
#
# conn.commit()
# conn.close()

