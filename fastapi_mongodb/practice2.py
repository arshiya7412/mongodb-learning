import os
from dotenv import load_dotenv
from pymongo import MongoClient
from fastapi import FastAPI
from pydantic import BaseModel
from bson import ObjectId
load_dotenv()
token = os.getenv("MONGODB_URI")
client = MongoClient(token)
db = client["mongodb-learning"]
items = db["items"]

app = FastAPI()

@app.get("/")
def home():
    return{"message": "Database created successfully"}

class Items(BaseModel):
    name: str
    price: int
    category: str

@app.post("/items")
def create_items(item: Items):
    result = items.insert_one(item.model_dump())
    return {"message": "Database connected successfully",
            "id": str(result.inserted_id)}

@app.get("/items")
def get_items():
    result1 = list(items.find({}, {"_id": 0}))
    return {"message": "Retrived items successfully",
            "id": result1}



