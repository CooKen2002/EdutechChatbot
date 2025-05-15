# Frontend/Dockerfile
# Sử dụng hình ảnh Node.js nhẹ
FROM node:18-alpine

WORKDIR /app

# Sao chép package.json và cài đặt thư viện
COPY package*.json ./
RUN npm install

# Sao chép mã nguồn ứng dụng
COPY . .

# Build React app
RUN npm run build

# Cấu hình Nginx để chạy app
EXPOSE 80
CMD ["npx", "serve", "-s", "build"]
