from pymongo import MongoClient
MONGODB_URI = "mongodb+srv://arshiyasana2006_db_user:FzzFqcFeZdhpPUTs@cluster0.6hudpgy.mongodb.net"
client = MongoClient(MONGODB_URI)
db = client["mongodb_learning"]
users = db["users"]
result = users.insert_many([{
    "name": "Arshiya",
    "age": 21,
    "role": "AI Developer"
},
{
    "name": "Sara",
    "age": 21,
    "role": "Software Developer"
}])
print(result.inserted_ids)

#find_one
result = users.find_one({"age": 20})
print(result)

#find()
cursor = users.find()
for us in cursor:
    print(us)

#update_one()
user1 = users.update_one(
    {"name": "Sara"},
    {"$set":{"role": "AI Engineer"}}
)
print(user1)

#update_many()
user2 = users.update_many(
    {"age": 20},
    {"$set":{"role": "Developer"}}
)
print(user2.modified_count)