import os
from dotenv import load_dotenv
from pymongo import MongoClient
load_dotenv
token = os.getenv("MONGODB_URI")
client = MongoClient(token)
db = client["mongodb-learning"]
print("created successfully")