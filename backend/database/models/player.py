from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.db import Base


class Player(Base):
    __tablename__ = "players"

    # ================================
    # BASIC FIELDS
    # ================================
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    team = Column(String, nullable=False)

    # ================================
    # STATS
    # ================================
    runs = Column(Integer, default=0)
    matches_played = Column(Integer, default=0)
    average = Column(Integer, default=0)
    strike_rate = Column(Integer, default=0)

    wickets = Column(Integer, default=0)
    economy = Column(Integer, default=0)

    # ================================
    # RELATIONS
    # ================================
    match_stats = relationship("MatchPlayer", back_populates="player")

    # ================================
    # HELPER METHOD
    # ================================
    def __repr__(self):
        return f"<Player {self.name} ({self.team})>"