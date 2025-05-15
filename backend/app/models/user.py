# app/models/user.py

from app import db

class User(db.Document):
    email = db.StringField(required=True, unique=True)
    password = db.StringField(required=True)
    learning_progress = db.StringField()  # Trường lưu tiến độ học
    interests = db.ListField(db.StringField())  # Trường lưu sở thích người dùng (mới)
    learning_path = db.StringField()  # Hoặc đổi thành ListField, EmbeddedDocumentField tùy nhu cầu
    hooby = db.StringField()          # (có thể là hobby - sửa lại chính tả nếu cần)
    subj = db.StringField()
