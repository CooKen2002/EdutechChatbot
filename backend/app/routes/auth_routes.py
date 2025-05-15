# backend/app/routes/auth_routes.py
from flask import Blueprint, request, jsonify
from app.models.user import User  # Đảm bảo bạn đã định nghĩa model User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    if User.objects(email=email).first():
        return jsonify({"success": False, "message": "Email đã được sử dụng!"}), 400

    # Tạo người dùng mới
    user = User(email=email, password=password)
    user.save()
    return jsonify({"success": True, "user": {"email": user.email}}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    # Sử dụng MongoEngine để truy vấn người dùng
    user = User.objects(email=email).first()

    if user and user.password == password:  # So khớp mật khẩu
        return jsonify({"success": True, "user": {"email": user.email}}), 200
    else:
        return jsonify({"success": False, "message": "Đăng nhập thất bại!"}), 401
