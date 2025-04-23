from datetime import datetime
from db import users, conversations

def get_or_create_user(user_id):
    user = users.find_one({"user_id": user_id})
    if not user:
        user = {"user_id": user_id, "created_at": datetime.now()}
        users.insert_one(user)
    return user

def save_conversation(user_id, user_message, bot_response):
    conversations.insert_one({
        "user_id": user_id,
        "user_message": user_message,
        "bot_response": bot_response,
        "timestamp": datetime.now()
    })
