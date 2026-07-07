import React, { useState } from "react";
import { getPlayerStats } from "../api/apiService";

function PlayerStats() {
  const [name, setName] = useState("");
  const [data, setData] = useState(null);

  const handleSearch = async () => {
    try {
      const res = await getPlayerStats(name);

      console.log("PLAYER DATA:", res);

      //  FIX: players array handle karo
      if (res?.players && res.players.length > 0) {
        setData(res.players[0]);
      } else {
        setData(null);
      }

    } catch (err) {
      console.error(err);
      setData(null);
    }
  };

  return (
    <div>
      <h2>👤 Player Stats</h2>

      <input
        value={name}
        onChange={(e) => setName(e.target.value)}
        placeholder="Enter player name"
      />
      <button onClick={handleSearch}>Search</button>

      {data ? (
        <div>
          <p>Name: {data.name}</p>
          <p>Team: {data.team}</p>
          <p>Runs: {data.runs}</p>
          <p>Avg: {data.avg}</p>
          <p>SR: {data.sr || "N/A"}</p>
        </div>
      ) : (
        <p>No data found</p>
      )}
    </div>
  );
}

export default PlayerStats;
