from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database.db import Base


class Record(Base):
    __tablename__ = "records"

    # ================================
    # BASIC
    # ================================
    id = Column(Integer, primary_key=True, index=True)

    match_id = Column(Integer, ForeignKey("matches.id"))
    player_id = Column(Integer, ForeignKey("players.id"))

    # ================================
    # PERFORMANCE
    # ================================
    runs = Column(Integer, default=0)
    balls = Column(Integer, default=0)

    wickets = Column(Integer, default=0)
    overs = Column(String, default="0")

    catches = Column(Integer, default=0)
    run_outs = Column(Integer, default=0)

    # ================================
    # EXTRA STATS
    # ================================
    strike_rate = Column(Integer, default=0)
    economy = Column(Integer, default=0)

    # ================================
    # META
    # ================================
    created_at = Column(DateTime, default=datetime.utcnow)

    # ================================
    # RELATIONSHIPS
    # ================================
    match = relationship("Match")
    player = relationship("Player")

    # ================================
    # HELPER
    # ================================
    def __repr__(self):
        return f"<Record Player={self.player_id} Match={self.match_id}>"