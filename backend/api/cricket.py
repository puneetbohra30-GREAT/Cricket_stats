from fastapi import APIRouter, Query, HTTPException
from typing import Optional
from datetime import datetime, timedelta
import random

router = APIRouter(prefix="/cricket")  # ✅ FIXED PREFIX

TEAMS = ["CSK", "MI", "RCB", "KKR", "GT", "LSG", "SRH", "DC"]

PLAYERS = [
    {"name": "Virat Kohli", "team": "RCB", "runs": 7500, "avg": 52},
    {"name": "MS Dhoni", "team": "CSK", "runs": 5000, "avg": 39},
    {"name": "Rohit Sharma", "team": "MI", "runs": 6200, "avg": 45},
    {"name": "KL Rahul", "team": "LSG", "runs": 4100, "avg": 47},
]

VENUES = ["Mumbai", "Delhi", "Chennai", "Kolkata"]


# ✅ LIVE MATCHES (NO AUTH FOR NOW)
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
