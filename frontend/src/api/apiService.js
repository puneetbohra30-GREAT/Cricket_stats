import API from "./api";

// ===============================
// AUTH APIs
// ===============================
export const login = async (data) => {
  const res = await API.post("/auth/login", data);
  console.log("✅ LOGIN API:", res.data);
  return res.data;
};

export const register = async (data) => {
  const res = await API.post("/auth/register", data);
  console.log("✅ REGISTER API:", res.data);
  return res.data;
};

// ===============================
// USER APIs
// ===============================
export const getProfile = async (username) => {
  if (!username) return null;

  const res = await API.get(`/user/${username.trim()}`);
  return res.data;
};

// ===============================
// CRICKET APIs
// ===============================
export const getLiveMatches = async () => {
  const res = await API.get("/cricket/live");
  return res.data;
};

export const getPlayerStats = async (name) => {
  if (!name) return null;

  const res = await API.get(`/cricket/player?name=${name}`);
  return res.data;
};

export const getSchedule = async () => {
  const res = await API.get("/cricket/schedule");
  return res.data;
};

// ===============================
// CHAT API (FIXED)
// ===============================
export const sendChat = async (message) => {
  if (!message) return null;

  const res = await API.post("/chat/", {
    message: message   // ✅ FIXED
  });

  console.log("✅ CHAT API:", res.data);

  return res.data;
};

// ===============================
// INSIGHTS API
// ===============================
export const getInsights = async (player) => {
  if (!player) return null;

  const res = await API.get(`/insights?player=${player}`);
  return res.data;
};

// ===============================
// KNOWLEDGE API
// ===============================
export const searchKnowledge = async (query) => {
  if (!query) return null;

  const res = await API.get(`/knowledge?q=${query}`);
  return res.data;
};