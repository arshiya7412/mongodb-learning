import os
from dotenv import load_dotenv
from pymongo import MongoClient
load_dotenv
token_1 = os.getenv("MONGODB_URI")
client = MongoClient(token_1)
db = client["mongodb-learning"]
print("created successfully")