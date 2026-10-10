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

for user in users.find().limit(2):
    print(user)

for skip in users.find().skip(1):
    print(skip)
