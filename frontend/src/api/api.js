import axios from "axios";

// ==============================
// BASE API INSTANCE
// ==============================
const API = axios.create({
  baseURL: "[https://cricket-stats-8i7l.onrender.com](https://cricket-stats-8i7l.onrender.com)", //  backend
  timeout: 15000,
  headers: {
    "Content-Type": "application/json",
  },
});

// ==============================
// REQUEST INTERCEPTOR
// ==============================
API.interceptors.request.use(
  (config) => {
    try {
      const token = localStorage.getItem("token");

      if (token) {
        config.headers.Authorization = `Bearer ${token}`;
      }

      console.log("➡️ REQUEST:", config.method?.toUpperCase(), config.url);
      return config;
    } catch (err) {
      console.error("Request Error:", err);
      return config;
    }
  },
  (error) => Promise.reject(error)
);

// ==============================
// RESPONSE INTERCEPTOR
// ==============================
API.interceptors.response.use(
  (response) => {
    console.log(" RESPONSE:", response.config.url);
    return response;
  },
  (error) => {
    console.error(" API ERROR:", error?.response?.data || error.message);

    //  TOKEN EXPIRED / UNAUTHORIZED
    if (error?.response?.status === 401) {
      localStorage.removeItem("token");
      alert("Session expired, please login again ");
      window.location.href = "/auth";
    }

    return Promise.reject(error);
  }
);

export default API;
