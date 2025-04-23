# backend/db.py
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["edutech_chatbot"]

users = db["users"]
conversations = db["conversations"]
