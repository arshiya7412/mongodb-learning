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

equality = users.find({"age": 21})
for eq in equality:
    print(eq)

grt_t = users.find({"age": {"$gt": 20}})
for gt in grt_t:
    print(gt)

grt_et = users.find({"age": {"$gte": 20}})
for grte in grt_et:
    print(grte)

ls_t = users.find({"age": {"$lt": 21}})
for lst in ls_t:
    print(lst)

nt_e = users.find({"age":{"$ne": 25}})
for nte in nt_e:
    print(nte)

an_d = users.find({"$and":[
    {"age": {"$gt": 20}},
    {"age": {"$lt": 25}}
]})
for a_nd in an_d:
    print(a_nd)

o_r = users.find({"or":
                  [{"age": {"$gt": 21}},
                   {"role": "Data Developer"}]})
for or_ in o_r:
    print(or_)

nested = users.find({"address.city": "Chennai"})
for nes in nested:
    print(nes)

arrays = users.find({"skills": "MongoDB"})
for array in arrays:
    print(array)

ex = users.find({"address": {"$exists": True}})
for exi in ex:
    print(exi)