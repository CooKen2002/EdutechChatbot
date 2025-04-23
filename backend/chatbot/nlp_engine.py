def process_user_message(message):
    msg = message.lower()

    if "python" in msg:
        return "Bạn muốn học Python à? Bạn có thể nói rõ mục tiêu học tập không?"
    elif "mục tiêu" in msg or "học để" in msg:
        return "Cảm ơn bạn! Mình sẽ tạo lộ trình học phù hợp cho bạn."
    elif "hello" in msg or "xin chào" in msg:
        return "Chào bạn! Mình là trợ lý học tập. Bạn đang muốn học kỹ năng gì?"
    else:
        return "Bạn có thể chia sẻ mục tiêu học tập hoặc kỹ năng bạn quan tâm không?"
