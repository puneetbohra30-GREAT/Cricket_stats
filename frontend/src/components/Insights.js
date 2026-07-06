import React, { useState } from "react";
import { getInsights } from "../api/apiService";

function Insights() {
  const [player, setPlayer] = useState("");
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);

  const fetchInsights = async () => {
    if (!player.trim()) return;

    setLoading(true);

    try {
      const res = await getInsights(player);
      console.log("INSIGHTS:", res);
      setData(res);
    } catch (err) {
      console.error(err);
      setData(null);
    }

    setLoading(false);
  };

  return (
    <div>
      <h2>📊 AI Insights</h2>

      {/* INPUT */}
      <input
        value={player}
        onChange={(e) => setPlayer(e.target.value)}
        placeholder="Enter player name"
      />

      <button onClick={fetchInsights} disabled={loading}>
        {loading ? "Loading..." : "Get Insights"}
      </button>

      {/* RESULT */}
      {data && (
        <div className="card">
          <h3>👤 {data.player}</h3>

          <p style={{ whiteSpace: "pre-line" }}>
            {data.analysis}
          </p>

          <p>🔥 Confidence: {data.confidence}</p>
          <p>⏱ {data.generated_at}</p>
        </div>
      )}

      {/* EMPTY */}
      {!loading && data === null && (
        <p>No data yet...</p>
      )}
    </div>
  );
}

export default Insights;