// ===============================
// IMPORTS
// ===============================
import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";

// Global CSS
import "./styles/main.css";


// ===============================
// ROOT RENDER
// ===============================
const root = ReactDOM.createRoot(
  document.getElementById("root")
);

root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);


// ===============================
// OPTIONAL PERFORMANCE LOG
// ===============================
if (process.env.NODE_ENV === "development") {
  console.log("Cricket AI Frontend Running...");
}
