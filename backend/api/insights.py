from fastapi import APIRouter, Query, HTTPException
from services.ai_insights import generate_insight
from datetime import datetime
import random

router = APIRouter()

# ================================
# PLAYER AI INSIGHTS
# ================================
@router.get("/")
def player_insights(player: str = Query(..., description="Player name")):
    try:
        analysis = generate_insight(player)

        return {
            "player": player,
            "analysis": analysis,
            "confidence": f"{random.randint(80, 98)}%",
            "generated_at": datetime.now().isoformat()
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ================================
# TEAM INSIGHTS
# ================================
@router.get("/team")
def team_insights(team: str = Query(...)):
    strengths = ["Batting", "Bowling", "All-round"]
    weaknesses = ["Top order", "Middle order", "Death bowling"]

    return {
        "team": team,
        "analysis": f"{team} has shown strong performance recently.",
        "strength": random.choice(strengths),
        "weakness": random.choice(weaknesses),
        "form": [random.randint(0, 100) for _ in range(5)]
    }


# ================================
# MATCH PREDICTION
# ================================
@router.get("/predict")
def match_prediction(team1: str, team2: str):
    score1 = random.randint(140, 210)
    score2 = random.randint(140, 210)

    winner = team1 if score1 > score2 else team2

    return {
        "team1": team1,
        "team2": team2,
        "predicted_score": {
            team1: score1,
            team2: score2
        },
        "predicted_winner": winner,
        "confidence": f"{random.randint(60, 90)}%",
        "generated_at": datetime.now().isoformat()
    }


# ================================
# TRENDING PLAYERS
# ================================
@router.get("/trending")
def trending_players():
    players = ["Virat Kohli", "Rohit Sharma", "MS Dhoni", "KL Rahul"]

    return {
        "players": [
            {
                "name": p,
                "trend_score": random.randint(70, 100)
            }
            for p in players
        ]
    }