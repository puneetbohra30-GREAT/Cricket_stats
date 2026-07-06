# ================================
# SIMPLE KNOWLEDGE GRAPH (FREE)
# ================================

CRICKET_KG = {
    "virat kohli": {
        "team": "RCB",
        "role": "Batsman",
        "runs": 7500
    },
    "ms dhoni": {
        "team": "CSK",
        "role": "Wicketkeeper",
        "runs": 5000
    },
    "rohit sharma": {
        "team": "MI",
        "role": "Batsman",
        "runs": 6200
    }
}


def get_knowledge(query: str):
    """
    Basic knowledge graph lookup
    """
    q = query.lower()

    for key in CRICKET_KG:
        if key in q:
            return {
                "entity": key,
                "data": CRICKET_KG[key]
            }

    return {
        "message": "No structured knowledge found",
        "suggestion": "Try player name like Virat Kohli"
    }


# ================================
# RELATION FINDER
# ================================
def get_relationship(player: str):
    data = CRICKET_KG.get(player.lower())

    if not data:
        return None

    return f"{player} plays for {data['team']} as {data['role']}"