import os
import time
import socket
import datetime
from pymongo import MongoClient


hostname = "google.com"
response = os.system("ping -c 1 " + hostname)

def database_updates(ip , networkdate):

    client = MongoClient('localhost', 27017)
    db = client['networkdata']
    collec = db['networkstatus']
    docum = {"ip": ip, "currentdate": networkdate }
    collec.insert_one(docum)



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


