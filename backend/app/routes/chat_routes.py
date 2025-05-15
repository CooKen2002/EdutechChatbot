# backend/app/routes/chat_routes.py

from flask import Blueprint, request, jsonify
## from app.services.nlp_service import classify_intent
from app.services.user_service import get_user_info  # Đảm bảo đường dẫn import chính xác
from app.services.learning_path_service import generate_learning_path
from app.services.nlp_service import NLPModel

chat_bp = Blueprint('chat', __name__)

nlp_model = NLPModel()

@chat_bp.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    email = data.get("email", "")

    if not user_message:
        return jsonify({"response": "Vui lòng nhập nội dung."}), 400

    # Phân tích intent (mình giả định num_labels=2, bạn nên tinh chỉnh)
    nlp_result = nlp_model.predict(user_message)

    # Ví dụ: dựa vào kết quả dự đoán để quyết định trả lời
    # (Bạn nên tùy chỉnh logic dựa trên dữ liệu nhãn training của bạn)
    predictions = nlp_result.get("predictions", [])
    intent_label = predictions[0] if predictions else 0

    # Lấy thông tin người dùng
    user = get_user_info(email)

    if intent_label == 1:  # Giả sử label 1 là câu hỏi về lộ trình học
        learning_path = generate_learning_path(user)
        bot_response = f"Lộ trình học đề xuất: {learning_path}"
    else:
        # Trả lời mặc định hoặc có thể trả lời dựa trên user_message
        bot_response = f"Bạn vừa hỏi: {user_message}. Tôi sẽ cố gắng giúp bạn!"

    return jsonify({"response": bot_response})

@chat_bp.route('/user-info', methods=['GET'])
def get_user_information():
    try:
        email = request.args.get('email', "").strip()
        if not email:
            return jsonify({"success": False, "message": "Vui lòng cung cấp email."}), 400

        user = get_user_info(email)
        if user:
            return jsonify({
                "success": True,
                "data": {
                    "email": user.email,
                    "learning_progress": user.learning_progress
                }
            }), 200
        
        return jsonify({"success": False, "message": "Không tìm thấy thông tin người dùng."}), 404
    except Exception as e:
        print(f"[ERROR] Exception in user-info route: {str(e)}")
        return jsonify({"success": False, "message": "Lỗi server."}), 500


@chat_bp.route('/progress', methods=['GET'])
def get_progress():
    email = request.args.get('email', "").strip()
    if not email:
        return jsonify({"message": "Vui lòng cung cấp email."}), 400
    
    user = get_user_info(email)
    if user:
        return jsonify({"progress": user.learning_progress}), 200
    
    return jsonify({"message": "Không tìm thấy thông tin người dùng."}), 404

@chat_bp.route('/learning-path', methods=['POST'])
def get_learning_path():
    try:
        data = request.get_json()
        email = data.get('email', "").strip()
        if not email:
            return jsonify({"message": "Vui lòng cung cấp email."}), 400

        user = get_user_info(email)
        if user:
            learning_path = generate_learning_path(user)
            return jsonify({"learning_path": learning_path}), 200
        
        return jsonify({"message": "Không tìm thấy thông tin người dùng."}), 404
    
    except Exception as e:
        print(f"[ERROR] Exception in learning-path route: {str(e)}")
        return jsonify({"message": "Đã xảy ra lỗi trong xử lý yêu cầu."}), 500
