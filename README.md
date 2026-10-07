# MongoDB — 1-Day Learning Roadmap

A one-day, hands-on MongoDB learning roadmap focused on **Python, PyMongo, and FastAPI integration**.

---

## 🟢 01 — MongoDB Fundamentals

- [ ] What is MongoDB?
- [ ] SQL vs NoSQL
- [ ] Database
- [ ] Collection
- [ ] Document
- [ ] Field
- [ ] `_id` and ObjectId
- [ ] BSON vs JSON
- [ ] MongoDB Atlas
- [ ] Connect to a MongoDB database

**Goal:** Understand how MongoDB stores data.

```text
Database
 └── Collection
      └── Document
           ├── _id
           ├── name
           └── age
```

---

## 🟢 02 — CRUD Operations ⭐

- [ ] `insert_one()`
- [ ] `insert_many()`
- [ ] `find_one()`
- [ ] `find()`
- [ ] `update_one()`
- [ ] `update_many()`
- [ ] `delete_one()`
- [ ] `delete_many()`

**Practice:** Build a `users` collection and perform complete CRUD.

---

## 🟢 03 — Querying & Filtering ⭐

- [ ] Equality filtering
- [ ] Comparison operators
- [ ] `$gt`
- [ ] `$gte`
- [ ] `$lt`
- [ ] `$lte`
- [ ] `$ne`
- [ ] Logical operators
- [ ] `$and`
- [ ] `$or`
- [ ] Nested fields
- [ ] Arrays
- [ ] Check whether a field exists

Example:

```python
users.find({"age": {"$gte": 18}})
```

---

## 🟢 04 — Updating Documents

- [ ] `$set`
- [ ] `$unset`
- [ ] `$inc`
- [ ] `$push`
- [ ] `$pull`
- [ ] Updating nested fields
- [ ] `upsert`

Example:

```python
users.update_one(
    {"name": "Arshiya"},
    {"$set": {"role": "Developer"}}
)
```

---

## 🟡 05 — Sorting, Limiting & Pagination

- [ ] `sort()`
- [ ] `limit()`
- [ ] `skip()`
- [ ] Basic pagination
- [ ] Filtering + sorting together

Example:

```python
users.find().sort("age", -1).limit(10)
```

---

## 🟡 06 — Data Modeling ⭐

- [ ] Embedded documents
- [ ] Arrays inside documents
- [ ] Referencing documents
- [ ] When to embed vs reference
- [ ] Designing a simple schema

Example:

```json
{
  "name": "Sensor-01",
  "location": {
    "room": "Lab-A",
    "floor": 2
  },
  "readings": [
    {
      "temperature": 28.5,
      "humidity": 65
    }
  ]
}
```

This is particularly useful for **device/sensor applications**.

---

## 🟡 07 — Python + MongoDB ⭐⭐⭐

Learn **PyMongo**:

- [ ] Install PyMongo
- [ ] Create MongoDB client
- [ ] Connect to database
- [ ] Select collection
- [ ] Insert from Python
- [ ] Read from Python
- [ ] Update from Python
- [ ] Delete from Python
- [ ] Convert MongoDB results into Python dictionaries
- [ ] Handle `ObjectId`

Basic structure:

```python
from pymongo import MongoClient

client = MongoClient(MONGO_URI)

db = client["my_database"]

users = db["users"]
```

---

## 🟢 08 — MongoDB + FastAPI ⭐⭐⭐

This is the **most important section** for backend/AI development.

- [ ] Connect FastAPI to MongoDB
- [ ] Create a POST endpoint
- [ ] Store request data in MongoDB
- [ ] Create a GET endpoint
- [ ] Retrieve documents
- [ ] Create GET `/items/{id}`
- [ ] Update with PUT/PATCH
- [ ] Delete with DELETE
- [ ] Handle `ObjectId`
- [ ] Handle MongoDB errors
- [ ] Use Pydantic models with MongoDB

### Target API

```text
POST   /devices
GET    /devices
GET    /devices/{id}
PUT    /devices/{id}
DELETE /devices/{id}
```

MongoDB should actually store the data.

---

## 🟡 09 — Indexing & Performance

Only learn the basics today:

- [ ] What is an index?
- [ ] Why indexes improve queries
- [ ] Create an index
- [ ] Unique index
- [ ] Basic idea of `explain()`

> **Don't deep-dive into database optimization today.**

---

## 🟡 10 — Environment & Security

- [ ] `.env` files
- [ ] Store MongoDB URI in environment variables
- [ ] Never hardcode credentials
- [ ] Basic connection error handling

---

# 🎯 Final Goal

By the end of this one-day sprint, build a working:

## FastAPI + PyMongo + MongoDB CRUD API

```text
Client
   ↓
FastAPI
   ↓
Pydantic
   ↓
PyMongo
   ↓
MongoDB
```

### Final Skills

By completing this roadmap, I should be able to:

- Understand MongoDB's document-based data model
- Perform CRUD operations
- Query and filter MongoDB documents
- Design basic MongoDB schemas
- Use MongoDB from Python with PyMongo
- Connect MongoDB with FastAPI
- Build REST APIs backed by MongoDB
- Handle MongoDB `ObjectId`
- Use environment variables securely
- Understand basic MongoDB indexing
- Build a complete device/sensor CRUD backend

---

## 🚀 Learning Method

Each module will follow:

**Concept → Example → Coding Task → Evaluation → Documentation → GitHub Commit → Next Module**

The goal is to learn MongoDB **by building**, not by memorizing syntax.
