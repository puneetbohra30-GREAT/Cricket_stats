from database.db import SessionLocal
from database.models.user import User
from database.models.player import Player
from database.models.match import Match
from utils.auth_utils import hash_password


def seed_data():
    db = SessionLocal()

    # -------------------------------
    # USERS
    # -------------------------------
    if not db.query(User).first():
        user = User(
            username="admin",
            email="admin@test.com",
            password=hash_password("admin123"),
            role="admin"
        )
        db.add(user)

    # -------------------------------
    # PLAYERS
    # -------------------------------
    if not db.query(Player).first():
        players = [
            Player(name="Virat Kohli", team="RCB", runs=7500),
            Player(name="MS Dhoni", team="CSK", runs=5000),
            Player(name="Rohit Sharma", team="MI", runs=6200)
        ]
        db.add_all(players)

    # -------------------------------
    # MATCHES
    # -------------------------------
    if not db.query(Match).first():
        match = Match(
            team1="RCB",
            team2="MI",
            venue="Mumbai",
            date="2026-07-04"
        )
        db.add(match)

    db.commit()
    db.close()

    print("✅ Seed data inserted!")


if __name__ == "__main__":
    seed_data()