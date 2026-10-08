import os
from dotenv import load_dotenv
from pymongo import MongoClient
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent / ".env"

print("Looking for .env at:", env_path)
print(".env exists:", env_path.exists())

load_dotenv(env_path)

token = os.getenv("MONGODB_URI")

print("URI loaded:", token is not None)
print("URI starts with:", token[:20] if token else None)

client = MongoClient(token)
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