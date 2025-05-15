import React, { useState } from "react";

const Login = ({ onLogin, onToggleToRegister }) => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Gửi yêu cầu đăng nhập đến backend
    const response = await fetch("http://localhost:5000/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ email, password }),
    });

    const data = await response.json();
    if (data.success) {
      onLogin(data.user);  // Gọi callback onLogin để lưu thông tin người dùng
    } else {
      alert("Đăng nhập thất bại!");
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
