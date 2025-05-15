import React, { useState } from "react";

const Register = ({ onRegister, onToggleToLogin }) => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Kiểm tra mật khẩu xác nhận
    if (password !== confirmPassword) {
      alert("Mật khẩu không khớp!");
      return;
    }

    // Gửi yêu cầu đăng ký đến backend
    const response = await fetch("http://localhost:5000/register", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ email, password }),
    });

    const data = await response.json();
    if (data.success) {
      onRegister(data.user);  // Gọi callback onRegister để lưu thông tin người dùng
    } else {
      alert("Đăng ký thất bại!");
    }
  };

  return (
    <div className="container">
      <h2>Đăng Ký</h2>
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
        <input
          type="password"
          placeholder="Xác nhận mật khẩu"
          value={confirmPassword}
          onChange={(e) => setConfirmPassword(e.target.value)}
          required
        />
        <button type="submit">Đăng Ký</button>
        
        {/* Chuyển sang trang đăng nhập */}
        <button type="button" className="toggle-btn" onClick={onToggleToLogin}>
          Quay lại Đăng Nhập
        </button>
      </form>
    </div>
  );
};

export default Register;
