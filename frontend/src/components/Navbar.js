import React, { useEffect, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { jwtDecode } from "jwt-decode";

function Navbar() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [username, setUsername] = useState("");
  const navigate = useNavigate();

  // 🔥 AUTH CHECK + USERNAME
  useEffect(() => {
    const checkAuth = () => {
      const token = localStorage.getItem("token");

      if (token) {
        setIsLoggedIn(true);

        try {
          const decoded = jwtDecode(token);
          setUsername(decoded?.sub || "User"); // 👤 username from JWT
        } catch {
          setUsername("");
        }
      } else {
        setIsLoggedIn(false);
        setUsername("");
      }
    };

    checkAuth();

    // 🔥 REAL-TIME UPDATE (important)
    window.addEventListener("storage", checkAuth);

    return () => window.removeEventListener("storage", checkAuth);
  }, []);

  // 🔥 LOGOUT
  const handleLogout = () => {
    localStorage.removeItem("token");

    // 🔥 trigger update everywhere
    window.dispatchEvent(new Event("storage"));

    navigate("/auth");
  };

  return (
    <nav style={styles.nav}>
      <h2>🏏 Cricket AI</h2>

      <div style={styles.links}>
        <Link to="/">Live</Link>
        <Link to="/schedule">Schedule</Link>
        <Link to="/player">Player</Link>
        <Link to="/compare">Compare</Link>
        <Link to="/chat">Chat</Link>
        <Link to="/insights">Insights</Link>

        {/* 👤 USER INFO */}
        {isLoggedIn && (
          <span style={styles.user}>👤 {username}</span>
        )}

        {/* PROFILE */}
        {isLoggedIn && <Link to="/profile">Profile</Link>}

        {/* AUTH */}
        {isLoggedIn ? (
          <button onClick={handleLogout} style={styles.btn}>
            Logout
          </button>
        ) : (
          <Link to="/auth" style={styles.btn}>
            Login
          </Link>
        )}
      </div>
    </nav>
  );
}

// ==============================
// STYLES
// ==============================
const styles = {
  nav: {
    display: "flex",
    justifyContent: "space-between",
    padding: "15px",
    background: "#111",
    color: "#fff",
  },
  links: {
    display: "flex",
    gap: "15px",
    alignItems: "center",
  },
  btn: {
    background: "crimson",
    color: "white",
    border: "none",
    padding: "6px 12px",
    cursor: "pointer",
    textDecoration: "none",
  },
  user: {
    color: "lightgreen",
    fontWeight: "bold"
  }
};

export default Navbar;