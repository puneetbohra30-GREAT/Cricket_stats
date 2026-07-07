import random
from datetime import datetime

# ================================
# MOCK AI ANALYSIS ENGINE
# ================================

def generate_insight(player_name: str) -> str:
    """
    Generate AI-like cricket insights (FREE - no API used)
    """

    strengths = [
        "excellent batting technique",
        "strong cover drives",
        "consistent performance",
        "aggressive intent",
        "solid defense"
    ]

    weaknesses = [
        "struggles against spin",
        "inconsistent under pressure",
        "weak against short balls",
        "slow strike rotation"
    ]

    forms = [
        " in top form",
        "improving steadily",
        "inconsistent lately",
        "performing strongly"
    ]

    # Random analysis generation
    strength = random.choice(strengths)
    weakness = random.choice(weaknesses)
    form = random.choice(forms)

    analysis = f"""
Player: {player_name}

Current Form: {form}

Strength:
- {strength}

Weakness:
- {weakness}

AI Suggestion:
- Focus on improving weak areas
- Maintain consistency in upcoming matches

Generated at: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
"""

    return analysis.strip()
