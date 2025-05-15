# app/__init__.py
from flask import Flask
from flask_mongoengine import MongoEngine
from app.config import Config
from flask_cors import CORS

db = MongoEngine()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)  # Kết nối MongoDB

    # Đăng ký các route (auth và chat)
    from app.routes.auth_routes import auth_bp
    from app.routes.chat_routes import chat_bp
    app.register_blueprint(auth_bp, url_prefix='/')
    app.register_blueprint(chat_bp, url_prefix='/chat')

    return app

app = Flask(__name__)
CORS(app, supports_credentials=True)