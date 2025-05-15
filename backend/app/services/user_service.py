# backend/app/services/user_service.py

from app.models.chatlog import User  # Đảm bảo import đúng Model User

def get_user_info(email):
    """Truy vấn thông tin người dùng từ database theo email"""
    user = User.objects(email=email).first()  # Truy vấn MongoDB để lấy thông tin người dùng
    return user  # Trả về đối tượng người dùng nếu tìm thấy, nếu không sẽ là None
