import React, { useState } from "react";
import { getProfile } from "../api/apiService";

function Profile() {
  const [username, setUsername] = useState("");
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);

  const loadProfile = async () => {
    if (!username.trim()) return;

    setLoading(true);

    const res = await getProfile(username);
    console.log("PROFILE:", res);

    setData(res);
    setLoading(false);
  };

  return (
    <div>
      <h2>👤 Profile</h2>

      <input
        placeholder="Enter username"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />

      <button onClick={loadProfile}>
        {loading ? "Loading..." : "Load"}
      </button>

      {/* ✅ DATA SHOW */}
      {data && (
        <div className="card">
          <h3>{data.username}</h3>
          <p>Email: {data.email}</p>
          <p>ID: {data.id}</p>
          <p>Created: {data.created_at}</p>
        </div>
      )}

      {!data && !loading && <p>No data found</p>}
    </div>
  );
}

export default Profile;