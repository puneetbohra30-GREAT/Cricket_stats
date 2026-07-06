from fastapi import APIRouter
from datetime import datetime
import random

router = APIRouter()

# ================================
# SERVICE STATUS
# ================================
@router.get("/status")
def external_status():
    return {
        "service": "External APIs",
        "status": "running",
        "timestamp": datetime.now().isoformat()
    }


# ================================
# WEATHER (MOCK DATA - FREE)
# ================================
@router.get("/weather")
def get_weather():
    conditions = ["Sunny", "Cloudy", "Humid", "Rainy"]

    return {
        "location": "Cricket Stadium",
        "temperature": f"{random.randint(25, 38)}°C",
        "condition": random.choice(conditions),
        "humidity": f"{random.randint(40, 85)}%",
        "wind_speed": f"{random.randint(5, 20)} km/h",
        "updated_at": datetime.now().isoformat()
    }


# ================================
# LIVE NEWS (MOCK)
# ================================
@router.get("/news")
def get_news():
    headlines = [
        "🔥 India wins thriller in last over!",
        "💯 Virat Kohli scores another century",
        "🏆 IPL Final announced",
        "⚡ Young talent shines in debut match",
        "🎯 Bowler takes 5-wicket haul"
    ]

    return {
        "count": len(headlines),
        "news": [
            {
                "title": h,
                "time": datetime.now().strftime("%H:%M")
            }
            for h in headlines
        ]
    }


# ================================
# STADIUM INFO
# ================================
@router.get("/stadium")
def stadium_info():
    stadiums = [
        {"name": "Wankhede", "city": "Mumbai"},
        {"name": "Chepauk", "city": "Chennai"},
        {"name": "Eden Gardens", "city": "Kolkata"},
        {"name": "Arun Jaitley", "city": "Delhi"}
    ]

    s = random.choice(stadiums)

    return {
        "stadium": s["name"],
        "city": s["city"],
        "capacity": random.randint(30000, 80000),
        "pitch_type": random.choice(["Batting", "Bowling", "Balanced"]),
        "last_updated": datetime.now().isoformat()
    }