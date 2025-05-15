# backend/app/models/chatlog.py

from datetime import datetime
from app import db

class User(db.Document):
    email = db.StringField(required=True, unique=True)
    password = db.StringField(required=True)
    learning_progress = db.StringField()  # Ví dụ trường lưu tiến độ học

class Conversation(db.Document):
    user_id = db.StringField(required=True)
    user_message = db.StringField(required=True)
    bot_response = db.StringField(required=True)
    timestamp = db.DateTimeField(default=datetime.utcnow)
