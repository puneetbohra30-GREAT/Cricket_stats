// ===============================
// DATE FORMAT
// ===============================
export const formatDate = (dateStr) => {
  if (!dateStr) return "";

  const date = new Date(dateStr);
  return date.toLocaleDateString("en-IN", {
    day: "2-digit",
    month: "short",
    year: "numeric"
  });
};


// ===============================
// TIME FORMAT
// ===============================
export const formatTime = (dateStr) => {
  if (!dateStr) return "";

  const date = new Date(dateStr);
  return date.toLocaleTimeString("en-IN", {
    hour: "2-digit",
    minute: "2-digit"
  });
};


// ===============================
// SHORT TEXT (TRUNCATE)
// ===============================
export const truncateText = (text, length = 50) => {
  if (!text) return "";
  return text.length > length ? text.slice(0, length) + "..." : text;
};


// ===============================
// LOCAL STORAGE
// ===============================
export const setToken = (token) => {
  localStorage.setItem("token", token);
};

export const getToken = () => {
  return localStorage.getItem("token");
};

export const logout = () => {
  localStorage.removeItem("token");
};


// ===============================
// NUMBER FORMAT
// ===============================
export const formatNumber = (num) => {
  if (!num) return 0;
  return num.toLocaleString();
};


// ===============================
// LOADING DELAY (UI EFFECT)
// ===============================
export const delay = (ms) => {
  return new Promise((resolve) => setTimeout(resolve, ms));
};


// ===============================
// RANDOM COLOR (FOR UI TAGS)
// ===============================
export const randomColor = () => {
  const colors = ["#38bdf8", "#6366f1", "#22c55e", "#f59e0b"];
  return colors[Math.floor(Math.random() * colors.length)];
};


// ===============================
// ERROR HANDLER
// ===============================
export const handleError = (err) => {
  console.error(err);
  return err?.response?.data?.detail || "Something went wrong";
};


// ===============================
// SUCCESS MESSAGE
// ===============================
export const successMsg = (msg) => {
  return {
    type: "success",
    message: msg
  };
};


// ===============================
// SIMPLE VALIDATION
// ===============================
export const isEmpty = (val) => {
  return !val || val.trim() === "";
};