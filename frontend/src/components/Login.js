import React, { useState } from "react";
import axios from "axios";

const Login = ({ onLogin, onToggleToRegister }) => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      // Gửi yêu cầu đăng nhập đến backend
      const response = await axios.post("http://localhost:5000/api/auth/login", {
        email,
        password,
      });

      if (response.data.success) {
        onLogin(response.data.user);  // Gọi callback onLogin để lưu thông tin người dùng
      } else {
        alert("Đăng nhập thất bại!");
      }
    } catch (error) {
      console.error("Lỗi kết nối API:", error);
      alert("Đăng nhập thất bại! Đã xảy ra lỗi.");
    }
  };
  
  return (
    <div className="container">
      <h2>Đăng Nhập</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
        <input
          type="password"
          placeholder="Mật khẩu"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        <button type="submit">Đăng Nhập</button>
        
        {/* Quên mật khẩu */}
        <div className="forgot-password">
          <a href="/forgot-password">Quên mật khẩu?</a>
        </div>

        {/* Dấu phân cách */}
        <hr />

        {/* Chuyển sang trang đăng ký */}
        <button type="button" className="toggle-btn" onClick={onToggleToRegister}>
          Đăng Ký
        </button>
      </form>
    </div>
  );
};

export default Login;
