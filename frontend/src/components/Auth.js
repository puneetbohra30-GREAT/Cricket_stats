import React, { useState, useEffect } from "react";
import { login, register } from "../api/apiService";
import { useNavigate } from "react-router-dom";

function Auth() {
  const navigate = useNavigate();

  const [form, setForm] = useState({
    username: "",
    email: "",
    password: ""
  });

  const [isLogin, setIsLogin] = useState(true);
  const [loading, setLoading] = useState(false);

  // 🔥 AUTO REDIRECT (already logged in)
  useEffect(() => {
    const token = localStorage.getItem("token");
    if (token) {
      navigate("/", { replace: true });
    }
  }, [navigate]);

  const submit = async () => {
    try {
      // ✅ VALIDATION
      if (!form.username || !form.password) {
        alert("Username & Password required ❌");
        return;
      }

      if (!isLogin && !form.email) {
        alert("Email required ❌");
        return;
      }

      setLoading(true);

      if (isLogin) {
        const res = await login({
          username: form.username.trim(),
          password: form.password
        });

        console.log("LOGIN RESPONSE:", res);

        const token = res?.access_token || res?.token;

        if (!token) {
          throw new Error("Token not received from server");
        }

        // ✅ SAVE TOKEN
        localStorage.setItem("token", token);

        // 🔥 FORCE NAVBAR UPDATE
        window.dispatchEvent(new Event("storage"));

        alert("Login Successful ✅");

        navigate("/", { replace: true });

      } else {
        await register({
          username: form.username.trim(),
          email: form.email.trim(),
          password: form.password
        });

        alert("Register Successful ✅, अब Login करो");

        setIsLogin(true);

        setForm({
          username: form.username,
          email: "",
          password: ""
        });
      }

    } catch (err) {
      console.error("Auth Error:", err);

      alert(
        err?.response?.data?.detail ||
        err.message ||
        "Something went wrong ❌"
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={styles.container}>
      <h2>{isLogin ? "🔐 Login" : "📝 Register"}</h2>

      <input
        placeholder="Username"
        value={form.username}
        onChange={(e) =>
          setForm({ ...form, username: e.target.value })
        }
        style={styles.input}
      />

      {!isLogin && (
        <input
          placeholder="Email"
          value={form.email}
          onChange={(e) =>
            setForm({ ...form, email: e.target.value })
          }
          style={styles.input}
        />
      )}

      <input
        placeholder="Password"
        type="password"
        value={form.password}
        onChange={(e) =>
          setForm({ ...form, password: e.target.value })
        }
        style={styles.input}
      />

      <button onClick={submit} disabled={loading} style={styles.btn}>
        {loading ? "Please wait..." : isLogin ? "Login" : "Register"}
      </button>

      <p style={styles.switch} onClick={() => setIsLogin(!isLogin)}>
        Switch to {isLogin ? "Register" : "Login"}
      </p>
    </div>
  );
}

// ================== STYLES ==================
const styles = {
  container: {
    padding: "30px",
    maxWidth: "400px",
    margin: "auto",
    textAlign: "center"
  },
  input: {
    width: "100%",
    padding: "10px",
    marginTop: "10px"
  },
  btn: {
    marginTop: "15px",
    width: "100%",
    padding: "10px",
    background: "crimson",
    color: "white",
    border: "none",
    cursor: "pointer"
  },
  switch: {
    cursor: "pointer",
    color: "blue",
    marginTop: "10px"
  }
};

export default Auth;