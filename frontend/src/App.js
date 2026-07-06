// ===============================
// IMPORTS
// ===============================
import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

// Components
import Navbar from "./components/Navbar";
import LiveScores from "./components/LiveScores";
import PlayerStats from "./components/PlayerStats";
import PlayerComparison from "./components/PlayerComparison";
import ChatBot from "./components/ChatBot";
import Insights from "./components/Insights";
import Schedule from "./components/Schedule";
import Profile from "./components/Profile";
import Auth from "./components/Auth";

// Styles
import "./styles/main.css";


// ===============================
// MAIN APP
// ===============================
function App() {
  return (
    <Router>
      <div className="app-container">

        {/* ===================== */}
        {/* NAVBAR */}
        {/* ===================== */}
        <Navbar />

        {/* ===================== */}
        {/* MAIN CONTENT */}
        {/* ===================== */}
        <div className="content">

          <Routes>

            {/* HOME - LIVE MATCHES */}
            <Route path="/" element={<LiveScores />} />

            {/* PLAYER STATS */}
            <Route path="/player" element={<PlayerStats />} />

            {/* PLAYER COMPARE */}
            <Route path="/compare" element={<PlayerComparison />} />

            {/* AI CHAT */}
            <Route path="/chat" element={<ChatBot />} />

            {/* AI INSIGHTS */}
            <Route path="/insights" element={<Insights />} />

            {/* MATCH SCHEDULE */}
            <Route path="/schedule" element={<Schedule />} />

            {/* USER PROFILE */}
            <Route path="/profile" element={<Profile />} />

            {/* AUTH */}
            <Route path="/auth" element={<Auth />} />

          </Routes>

        </div>

      </div>
    </Router>
  );
}

export default App;



// ===============================
// OPTIONAL: DASHBOARD WRAPPER UI
// ===============================
export function DashboardLayout({ children }) {
  return (
    <div className="dashboard">

      <div className="dashboard-header">
        <h2>🏏 Cricket AI Dashboard</h2>
      </div>

      <div className="dashboard-content">
        {children}
      </div>

    </div>
  );
}



// ===============================
// OPTIONAL: LOADING COMPONENT
// ===============================
export function Loader() {
  return (
    <div className="loader">
      <div className="spinner"></div>
      <p>Loading...</p>
    </div>
  );
}



// ===============================
// OPTIONAL: ERROR COMPONENT
// ===============================
export function ErrorBox({ message }) {
  return (
    <div className="error-box">
      <h3>⚠ Error</h3>
      <p>{message}</p>
    </div>
  );
}