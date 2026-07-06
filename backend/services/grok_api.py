import random

# ================================
# GROK STYLE AI (FREE MOCK)
# ================================

def grok_response(query: str) -> str:
    """
    Simulates Grok / LLM style responses
    """

    responses = [
        f"🤖 AI: Based on analysis, '{query}' shows strong cricket relevance.",
        f"📊 Insight: '{query}' is trending in recent matches.",
        f"🔥 Prediction: '{query}' could impact upcoming games.",
        f"💡 Suggestion: Focus on '{query}' for better performance.",
        f"⚡ Smart AI: '{query}' has strategic importance in cricket."
    ]

    return random.choice(responses)


# ================================
# INTENT DETECTION
# ================================
def detect_intent(query: str) -> str:
    query = query.lower()

    if "score" in query or "live" in query:
        return "live"
    elif "player" in query:
        return "player"
    elif "schedule" in query:
        return "schedule"
    elif "compare" in query:
        return "compare"
    else:
        return "general"