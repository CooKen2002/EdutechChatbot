// src/components/UserProfile.js
import React from "react";

function UserProfile({ userInfo }) {
  return (
    <div className="user-profile">
      <img src={userInfo.avatar} alt="User Avatar" />
      <h3>{userInfo.name}</h3>
    </div>
  );
}

export default UserProfile;
