# Backend/Dockerfile
# Sử dụng hình ảnh Python nhẹ
FROM python:3.10-slim

WORKDIR /app

# Cài đặt các thư viện yêu cầu
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Sao chép mã nguồn ứng dụng
COPY . .

# Expose port Flask
EXPOSE 5000

# Chạy Flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
