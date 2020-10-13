import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatastore"]
mycol = mydb["mycollection"]

myquery = { "age": "33" }

mycol.delete_one(myquery)