from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database.db import Base


class User(Base):
    __tablename__ = "users"

    # ================================
    # PRIMARY KEY
    # ================================
    id = Column(Integer, primary_key=True, index=True)

    # ================================
    # BASIC INFO
    # ================================
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(100), unique=True, nullable=False, index=True)
    password = Column(String(255), nullable=False)

    # ================================
    # META INFO
    # ================================
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    role = Column(String(20), default="user", nullable=False)

    # ================================
    # OPTIONAL PROFILE
    # ================================
    favorite_team = Column(String(50), nullable=True)

    # ================================
    # STRING REPRESENTATION
    # ================================
    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}')>"