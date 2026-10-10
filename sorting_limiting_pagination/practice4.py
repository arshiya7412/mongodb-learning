import os
from dotenv import load_dotenv
from pymongo import MongoClient, ASCENDING, DESCENDING

load_dotenv()

token  = os.getenv("MONGODB_URI")
client = MongoClient(token)
db = client["mongodb-learning"]
users = db["users"]

result =  users.insert_many([{
        "name": "Arshiya",
        "age": 21,
        "role": "AI Developer",
        "skills": ["Python", "MongoDB", "AI"],
        "address": {
            "city": "Chennai",
            "country": "India"
        }
    },
    {
        "name": "Sara",
        "age": 20,
        "role": "Software Developer",
        "skills": ["Python", "Java"],
        "address": {
            "city": "Bangalore",
            "country": "India"
        }
    },
    {
        "name": "Aisha",
        "age": 25,
        "role": "Data Scientist",
        "skills": ["Python", "ML"],
        "address": {
            "city": "Mumbai",
            "country": "India"
        }
    }
    
])

for user in users.find({"age":{"$gte": 21}}).sort("age", ASCENDING):
    print(user["age"])

for user in users.find({"age":{"$gte": 21}}).sort("age", DESCENDING):
    print(user)

for user in users.find({"age":{"$gte": 21}}).sort("age", ASCENDING).limit(3):
    print(user)

for user in users.find().sort("age", DESCENDING):
    print(user)

for user in users.find({"name": "Arshiya"}, {"address.city"}):
    print(user["address"]["city"])

student = users.find_one({"name": "Arshiya"})
student_1 = list(users.find())
if student:
    print(type(student))
    print(student["name"])
    print(student["_id"])
    print(student_1)
