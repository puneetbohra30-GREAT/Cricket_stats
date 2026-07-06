import random
from datetime import datetime, timedelta

# ================================
# MOCK LIVE MATCHES
# ================================
def get_live_matches():
    teams = ["CSK", "MI", "RCB", "KKR", "GT", "LSG"]

    matches = []

    for i in range(2):
        t1 = random.choice(teams)
        t2 = random.choice([t for t in teams if t != t1])

        matches.append({
            "match_id": i,
            "team1": t1,
            "team2": t2,
            "score": f"{random.randint(140, 200)}/{random.randint(3, 8)}",
            "overs": f"{random.randint(10, 20)}.{random.randint(0,5)}",
            "status": "Live",
            "time": datetime.now().strftime("%H:%M:%S")
        })

    return matches


# ================================
# MOCK PLAYER STATS
# ================================
def get_mock_player_stats(name: str):
    return {
        "name": name,
        "runs": random.randint(1000, 8000),
        "average": random.randint(30, 60),
        "strike_rate": random.randint(110, 180),
        "matches": random.randint(50, 300)
    }


# ================================
# MATCH SCHEDULE
# ================================
def get_match_schedule(days: int = 5):
    teams = ["CSK", "MI", "RCB", "KKR", "GT", "LSG"]

    schedule = []
    base = datetime.now()

    for i in range(days):
        t1 = random.choice(teams)
        t2 = random.choice([t for t in teams if t != t1])

        schedule.append({
            "match": i + 1,
            "team1": t1,
            "team2": t2,
            "date": (base + timedelta(days=i)).strftime("%d %b"),
            "venue": random.choice(["Mumbai", "Delhi", "Chennai"])
        })

    return schedule


# ================================
# TRENDING PLAYERS
# ================================
def get_trending_players():
    players = ["Virat Kohli", "Rohit Sharma", "MS Dhoni", "KL Rahul"]

    return [
        {
            "name": p,
            "trend_score": random.randint(70, 100)
        }
        for p in players
    ]