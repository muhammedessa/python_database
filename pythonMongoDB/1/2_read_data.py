#Find One

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatastore"]
mycol = mydb["mycollection"]

x = mycol.find_one()

print(x)





#Find All

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatastore"]
mycol = mydb["mycollection"]

for x in mycol.find():
  print(x)







