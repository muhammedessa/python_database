import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatastore"]
mycol = mydb["mycollection"]

myquery = { "name": "Ahmed Essa" }
newvalues = { "$set": { "age": "44" } }

mycol.update_one(myquery, newvalues)

#print "customers" after the update:
for x in mycol.find():
  print(x)