from flask import Blueprint, request, jsonify
from models.chatlog import get_or_create_user, save_conversation
from utils.bot import process_user_message  

chat_bp = Blueprint("chat", __name__)  

@chat_bp.route("/", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    user_id = data.get("user_id", "default_user")  # tạm hardcode nếu chưa có auth

    user = get_or_create_user(user_id)
    bot_response = process_user_message(user_message)

    # Lưu vào DB
    save_conversation(user_id, user_message, bot_response)

    return jsonify({
        "user": user_message,
        "bot": bot_response
    })
