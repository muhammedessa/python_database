#pip install pymongo

from pymongo import MongoClient

#Creating a pymongo client
client = MongoClient('localhost', 27017)

#Getting the database instance
db = client['mydatastore']

#Creating a collection
collec = db['mycollection']

#Inserting document into a collection
docum = {"name": "Ahmed Essa", "age": "33", "province": "Kirkuk"}
collec.insert_one(docum)
print(collec.find_one())







