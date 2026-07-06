import React, { useState } from "react";
import { getPlayerStats } from "../api/apiService";

function PlayerComparison() {
  const [p1, setP1] = useState("");
  const [p2, setP2] = useState("");
  const [data, setData] = useState([]);

  const handleCompare = async () => {
    try {
      const res1 = await getPlayerStats(p1);
      const res2 = await getPlayerStats(p2);

      console.log("P1:", res1);
      console.log("P2:", res2);

      let player1 = res1?.players?.[0];
      let player2 = res2?.players?.[0];

      setData([player1, player2]);

    } catch (err) {
      console.error(err);
      setData([]);
    }
  };

  return (
    <div>
      <h2>⚔ Player Comparison</h2>

      <input
        placeholder="Player 1"
        value={p1}
        onChange={(e) => setP1(e.target.value)}
      />

      <input
        placeholder="Player 2"
        value={p2}
        onChange={(e) => setP2(e.target.value)}
      />

      <button onClick={handleCompare}>Compare</button>

      {data.length === 2 && data[0] && data[1] ? (
        <div style={{ display: "flex", gap: "40px", marginTop: "20px" }}>

          {/* Player 1 */}
          <div className="card">
            <h3>{data[0].name}</h3>
            <p>Runs: {data[0].runs}</p>
            <p>Avg: {data[0].avg}</p>
            <p>SR: {data[0].sr || "N/A"}</p>
          </div>

          {/* Player 2 */}
          <div className="card">
            <h3>{data[1].name}</h3>
            <p>Runs: {data[1].runs}</p>
            <p>Avg: {data[1].avg}</p>
            <p>SR: {data[1].sr || "N/A"}</p>
          </div>

        </div>
      ) : (
        <p>No data</p>
      )}
    </div>
  );
}

export default PlayerComparison;