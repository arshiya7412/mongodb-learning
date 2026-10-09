import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

token = os.getenv("MONGODB_URI")
client = MongoClient(token)
db = client["mongodb-learning"]
users = db["users"]

result = users.insert_many([{
    "name": "Arshiya",
    "age": 21,
    "role": "AI Developer",
    "skills": ["Python", "MongoDB"],
    "address": {
        "city": "Chennai",
        "country": "India"
    }
}])

#$set
set = users.update_one(
    {"name": "Arshiya"},
    {"$set": {"gender": "Female"}})

print(set)

#$unset
unset = users.update_one(
    {"name": "Arshiya"},
    {"$unset": {"gender": "Female"}}
)
print(unset)