from fastapi import APIRouter, Query, HTTPException
from typing import Optional
from datetime import datetime, timedelta
import random

# ❌ prefix हटाओ
router = APIRouter(tags=["Cricket"])


TEAMS = ["CSK", "MI", "RCB", "KKR", "GT", "LSG", "SRH", "DC"]

PLAYERS = [
    {"name": "Virat Kohli", "team": "RCB", "runs": 7500, "avg": 52},
    {"name": "MS Dhoni", "team": "CSK", "runs": 5000, "avg": 39},
    {"name": "Rohit Sharma", "team": "MI", "runs": 6200, "avg": 45},
    {"name": "KL Rahul", "team": "LSG", "runs": 4100, "avg": 47},
]

VENUES = ["Mumbai", "Delhi", "Chennai", "Kolkata"]


# -------------------------------
# LIVE MATCHES
# -------------------------------
@router.get("/live")
def live_matches(limit: int = 2):
    matches = []

    for i in range(limit):
        t1 = random.choice(TEAMS)
        t2 = random.choice([t for t in TEAMS if t != t1])

        matches.append({
            "id": i,
            "team1": t1,
            "team2": t2,
            "score": f"{random.randint(140,200)}/{random.randint(2,8)}",
            "overs": f"{random.randint(10,20)}.{random.randint(0,5)}",
            "venue": random.choice(VENUES),
            "status": "Live",
            "time": datetime.now().strftime("%H:%M:%S")
        })

    return {"matches": matches}


# -------------------------------
# SCHEDULE
# -------------------------------
@router.get("/schedule")
def schedule(days: int = 5):
    data = []
    base = datetime.now()

    for i in range(days):
        t1 = random.choice(TEAMS)
        t2 = random.choice([t for t in TEAMS if t != t1])

        data.append({
            "match": i,
            "team1": t1,
            "team2": t2,
            "date": (base + timedelta(days=i)).strftime("%d %b"),
            "venue": random.choice(VENUES)
        })

    return {"schedule": data}


# -------------------------------
# PLAYER SEARCH
# -------------------------------
@router.get("/player")
def player_search(name: str = Query(...), min_runs: Optional[int] = None):
    result = []

    for p in PLAYERS:
        if name.lower() in p["name"].lower():
            if min_runs and p["runs"] < min_runs:
                continue
            result.append(p)

    return {"players": result}


# -------------------------------
# PLAYER DETAIL
# -------------------------------
@router.get("/player/{name}")
def player_detail(name: str):
    for p in PLAYERS:
        if name.lower() in p["name"].lower():
            return {
                **p,
                "form": [random.randint(0, 100) for _ in range(5)]
            }

    raise HTTPException(status_code=404, detail="Player not found")


# -------------------------------
# TEAM STATS
# -------------------------------
@router.get("/team/{team}")
def team_stats(team: str):
    team_players = [p for p in PLAYERS if p["team"] == team]

    if not team_players:
        raise HTTPException(status_code=404, detail="Team not found")

    total_runs = sum(p["runs"] for p in team_players)

    return {
        "team": team,
        "players": team_players,
        "total_runs": total_runs
    }


# -------------------------------
# MATCH SIMULATION
# -------------------------------
@router.get("/simulate")
def simulate(team1: str, team2: str):
    score1 = random.randint(140, 220)
    score2 = random.randint(140, 220)

    winner = team1 if score1 > score2 else team2

    return {
        "team1": team1,
        "team2": team2,
        "score1": score1,
        "score2": score2,
        "winner": winner
    }


# -------------------------------
# STATS
# -------------------------------
@router.get("/stats")
def stats():
    return {
        "total_matches": random.randint(1000, 5000),
        "total_runs": random.randint(50000, 100000)
    }
