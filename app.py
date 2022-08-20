from random import randint

from pymongo import MongoClient

# cluster = MongoClient("mongodb+srv://Shkum:<password>@cluster0.pmqs4wy.mongodb.net/?retryWrites=true&w=majority")
# add info path to DB in < >
cluster = MongoClient("mongodb+srv://Shkum:Angelina_1@cluster0.pmqs4wy.mongodb.net/?retryWrites=true&w=majority")

# db = cluster.testdata
db = cluster['testdata']

# collection = db.testcoll
collection = db['testcoll']

name = input("> ")
collection.insert_one({'_id':1, 'name': name, 'balance': randint(1, 100)})
