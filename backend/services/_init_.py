# ================================
# SERVICES PACKAGE INIT
# ================================

from .ai_insights import generate_insight
from .data_scraping import (
    get_live_matches,
    get_mock_player_stats,
    get_match_schedule
)

__all__ = [
    "generate_insight",
    "get_live_matches",
    "get_mock_player_stats",
    "get_match_schedule"
]