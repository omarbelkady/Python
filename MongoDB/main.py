from pymongo import *
#Instantiating a mongo client
client = MongoClient("mongodb+srv://admin:admin@omarscluster.rdtkc.mongodb.net/pintosDBLover?retryWrites=true&w=majority")
#Creating a db
db=client["pintosDBLover"]
collection=db["collection"]
collection.insert_one({"favParad":"Imperative"})
