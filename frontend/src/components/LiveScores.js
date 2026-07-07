import React, { useEffect, useState } from "react";
import { getLiveMatches } from "../api/apiService";

function LiveScores() {
  const [matches, setMatches] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchMatches = async () => {
      try {
        const res = await getLiveMatches();

        console.log("API RESPONSE:", res);

        //  HANDLE ALL CASES
        if (Array.isArray(res)) {
          setMatches(res);
        } else if (Array.isArray(res?.matches)) {
          setMatches(res.matches);
        } else if (Array.isArray(res?.data)) {
          setMatches(res.data);
        } else {
          setMatches([]);
        }

      } catch (err) {
        console.error("Fetch Error:", err);
        setMatches([]);
      } finally {
        setLoading(false);
      }
    };

    fetchMatches();
  }, []);

  return (
    <div>
      <h2>🔥 Live Matches</h2>

      {loading ? (
        <p>Loading...</p>
      ) : matches.length === 0 ? (
        <p>No live matches found</p>
      ) : (
        matches.map((m, i) => (
          <div key={i} className="card">
            <h3>{m?.team1 || "Team A"} vs {m?.team2 || "Team B"}</h3>
            <p>Score: {m?.score || "N/A"}</p>
            <p>Overs: {m?.overs || "N/A"}</p>
          </div>
        ))
      )}
    </div>
  );
}

export default LiveScores;
