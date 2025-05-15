# backend/app/services/learning_path_service.py

def generate_learning_path(user):
    if not user:
        return []

    # Phân tích sở thích người dùng (giả định là user có trường "interests")
    interests = getattr(user, "interests", "")
    learning_progress = getattr(user, "learning_progress", "")
    learning_path = []

    # Ví dụ về logic đề xuất lộ trình học tập
    if "Data Science" in interests:
        if "Python Basics" not in learning_progress:
            learning_path.append("Python Basics")
        if "Python Basics" in learning_progress and "Machine Learning" not in learning_progress:
            learning_path.append("Machine Learning")

    if "Web Development" in interests:
        if "HTML & CSS" not in learning_progress:
            learning_path.append("HTML & CSS")
        if "HTML & CSS" in learning_progress and "JavaScript" not in learning_progress:
            learning_path.append("JavaScript")

    if not learning_path:
        learning_path.append("Chưa có lộ trình học phù hợp. Hãy cập nhật sở thích của bạn.")

    return ", ".join(learning_path)
