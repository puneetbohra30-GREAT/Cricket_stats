from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.db import Base


class Match(Base):
    __tablename__ = "matches"

    # ================================
    # BASIC INFO
    # ================================
    id = Column(Integer, primary_key=True, index=True)
    team1 = Column(String, nullable=False)
    team2 = Column(String, nullable=False)
    venue = Column(String, nullable=False)
    date = Column(String)

    # ================================
    # SCORES
    # ================================
    score_team1 = Column(String, default="0/0")
    score_team2 = Column(String, default="0/0")

    result = Column(String, default="Pending")

    # ================================
    # RELATIONS
    # ================================
    players = relationship("MatchPlayer", back_populates="match")

    def __repr__(self):
        return f"<Match {self.team1} vs {self.team2}>"



# ==========================================
# MANY-TO-MANY TABLE (MATCH ↔ PLAYER)
# ==========================================
class MatchPlayer(Base):
    __tablename__ = "match_players"

    id = Column(Integer, primary_key=True, index=True)

    match_id = Column(Integer, ForeignKey("matches.id"))
    player_id = Column(Integer, ForeignKey("players.id"))

    # PERFORMANCE IN MATCH
    runs = Column(Integer, default=0)
    balls = Column(Integer, default=0)
    wickets = Column(Integer, default=0)
    overs = Column(String, default="0")

    # RELATIONS
    match = relationship("Match", back_populates="players")
    player = relationship("Player", back_populates="match_stats")

    def __repr__(self):
        return f"<MatchPlayer match={self.match_id} player={self.player_id}>"