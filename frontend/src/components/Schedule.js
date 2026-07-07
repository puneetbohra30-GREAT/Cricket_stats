import React, { useEffect, useState } from "react";
import { getSchedule } from "../api/apiService";

function Schedule() {
  const [matches, setMatches] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchData() {
      try {
        const res = await getSchedule();
        console.log("SCHEDULE:", res);

        // FIX HERE
        if (res && Array.isArray(res.schedule)) {
          setMatches(res.schedule);
        } else {
          setMatches([]);
        }

      } catch (err) {
        console.error("Schedule Error:", err);
        setMatches([]);
      } finally {
        setLoading(false);
      }
    }

    fetchData();
  }, []);

  return (
    <div>
      <h2>📅 Match Schedule</h2>

      {loading ? (
        <p>Loading...</p>
      ) : matches.length === 0 ? (
        <p>No matches found</p>
      ) : (
        matches.map((m, i) => (
          <div key={i} className="card">
            <h3>{m.team1} vs {m.team2}</h3>
            <p>📅 {m.date}</p>
            <p>🏟 {m.venue}</p>
          </div>
        ))
      )}
    </div>
  );
}

export default Schedule;
