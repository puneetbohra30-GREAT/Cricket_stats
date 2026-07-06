from services.grok_api import grok_response, detect_intent
from services.data_scraping import (
    get_live_matches,
    get_mock_player_stats,
    get_match_schedule
)
from services.knowledge_graph import get_knowledge

# ================================
# AGENT ROUTER (LANGCHAIN STYLE)
# ================================

def agent_router(query: str):
    """
    Decide which tool to use based on query
    """

    intent = detect_intent(query)

    # -------------------------------
    # LIVE MATCH
    # -------------------------------
    if intent == "live":
        matches = get_live_matches()
        return {
            "type": "live_matches",
            "data": matches
        }

    # -------------------------------
    # PLAYER INFO
    # -------------------------------
    elif intent == "player":
        data = get_mock_player_stats(query)
        return {
            "type": "player_stats",
            "data": data
        }

    # -------------------------------
    # SCHEDULE
    # -------------------------------
    elif intent == "schedule":
        schedule = get_match_schedule()
        return {
            "type": "schedule",
            "data": schedule
        }

    # -------------------------------
    # KNOWLEDGE GRAPH
    # -------------------------------
    elif intent == "general":
        knowledge = get_knowledge(query)

        if "entity" in knowledge:
            return {
                "type": "knowledge",
                "data": knowledge
            }

    # -------------------------------
    # FALLBACK AI
    # -------------------------------
    return {
        "type": "ai_response",
        "data": grok_response(query)
    }