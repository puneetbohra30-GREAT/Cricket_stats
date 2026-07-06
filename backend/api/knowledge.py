from fastapi import APIRouter, Query, HTTPException
from services.knowledge_graph import get_knowledge
from datetime import datetime

router = APIRouter()

# ================================
# MAIN KNOWLEDGE QUERY
# ================================
@router.get("/")
def knowledge_search(q: str = Query(..., description="Search query")):
    try:
        result = get_knowledge(q)

        return {
            "query": q,
            "result": result,
            "timestamp": datetime.now().isoformat()
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ================================
# FAQ (STATIC KNOWLEDGE)
# ================================
@router.get("/faq")
def get_faq():
    return {
        "faqs": [
            {
                "question": "What is strike rate?",
                "answer": "Strike rate = (Runs / Balls faced) × 100"
            },
            {
                "question": "What is powerplay?",
                "answer": "First 6 overs with fielding restrictions"
            },
            {
                "question": "What is net run rate?",
                "answer": "Measures team performance using run difference per over"
            }
        ]
    }


# ================================
# CRICKET RULES
# ================================
@router.get("/rules")
def cricket_rules():
    return {
        "rules": [
            "Each team has 11 players",
            "20 overs per side in T20",
            "Powerplay applies in first 6 overs",
            "No-ball gives free hit in limited overs"
        ]
    }


# ================================
# TERMS EXPLANATION
# ================================
@router.get("/terms")
def cricket_terms(term: str = Query(...)):
    glossary = {
        "strike rate": "Runs scored per 100 balls",
        "economy": "Runs conceded per over",
        "duck": "Batsman out on 0",
        "century": "100 runs by a batsman"
    }

    explanation = glossary.get(term.lower())

    if not explanation:
        raise HTTPException(status_code=404, detail="Term not found")

    return {
        "term": term,
        "meaning": explanation
    }