import os
from dotenv import load_dotenv
from pymongo import MongoClient
from fastapi import FastAPI
from pymongo.errors import PyMongoError

load_dotenv()

token = os.getenv("MONGODB_URI")
client = MongoClient(token)
db = client["mongodb-learning"]
items = db["items"]

app = FastAPI()
@app.get("/")
def home():
    return {"message": "FastAPI + MongoDB is running"}

@app.get("/health/db")
def check_db():
    try:
        client.admin.command("ping")
        return {"message": "database connected"}
    except PyMongoError:
        return {"database": "database error" }