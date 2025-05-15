# backend/app.py

from flask import Flask
from db import db  # Kết nối MongoDB từ db.py
from config import Config
from app.routes.chat_routes import chat_bp  # Import chat routes
from app.routes.auth_routes import auth_bp  # Import auth routes
from app.utils.cors import init_cors  # Chỉ sử dụng phương thức CORS đã tạo

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Khởi tạo CORS
    init_cors(app)

    # Khởi tạo MongoDB
    db.init_app(app)

    # Đăng ký các route với tiền tố /api
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(chat_bp, url_prefix='/api/')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)  # Đảm bảo có host và port chính xác
