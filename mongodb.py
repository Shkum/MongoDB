from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://Shkum:Angelina_1@cluster0.pmqs4wy.mongodb.net/?retryWrites=true&w=majority")

db = cluster['test']  # select DB

collection = db['test']  # select collection (Table)

post = {'_id': 1, "name": 'Serg'}  # usual variable name for post (inserting value(dictionary))
post1 = {'_id': 2, "name": 'Angel'}  # usual variable name for post (inserting value(dictionary))
post2 = {'_id': 3, "name": 'Angel'}  # usual variable name for post (inserting value(dictionary))

#  INSERT ONE NEW POST:
# collection.insert_one(post)  # insert value into collection (Table) - it is {dictionary}


# INSERT FEW NEW POSTS:
# collection.insert_many([post1, post2])


# FIND VALUE IN THE COLLECTION (TABLE)
results = collection.find({'name': 'Angel'})  # several items to search
for result in results:
    print(f"{result} -> {result['name']}")

print('*' * 50)

results = collection.find_one({'name': 'Angel'})  # one value to search
print(results)

print('*' * 50)

results = collection.find({})  # empty request to find will return all infor in the collection (Table)
for result in results:
    print(f"{result} -> {result['name']}")

# DELETE DATA FROM COLLECTION (TABLE)
# results = collection.delete_one({'_id': 2})

# result = collection.delete_many({'_id': 1, '_id': 2})


# UPDATE DATA IN THE COLLECTION (TABLE)
results = collection.update_one({"_id": 2}, {'$set': {'name': 'Angel'}})  # update value
results = collection.update_one({"_id": 2}, {'$set': {'sex': 'cool'}})  # add new value

# results = collection.update_many({"_id": 2}, {'$set': {'sex': 'cool'}})  # update few fields


# DELETE ONE VALUE FROM THE DOCUMENT (FIELD):
results = collection.update_many({'_id': 2}, {'$unset': {'sex': ''}})

# COUNT QUANTITY OF RECORDS (POSTS)
post_count = collection.count_documents({})
print(post_count)
