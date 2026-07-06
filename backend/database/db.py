# =========================
# IMPORTS (SAFE)
# =========================
import logging

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import SQLAlchemyError

from config import settings


# =========================
# LOGGER
# =========================
logger = logging.getLogger("database")
logging.basicConfig(level=logging.INFO)


# =========================
# DATABASE URL (SAFE FALLBACK)
# =========================
DATABASE_URL = getattr(settings, "DATABASE_URL", "sqlite:///./cricket.db")
logger.info(f"Using DB: {DATABASE_URL}")


# =========================
# ENGINE CONFIG
# =========================
engine_kwargs = {
    "echo": getattr(settings, "DB_ECHO", False),
}

# SQLite special config
if "sqlite" in DATABASE_URL:
    engine_kwargs["connect_args"] = {"check_same_thread": False}
else:
    engine_kwargs["pool_pre_ping"] = True


# =========================
# ENGINE
# =========================
engine = create_engine(DATABASE_URL, **engine_kwargs)


# =========================
# SESSION
# =========================
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# =========================
# BASE
# =========================
Base = declarative_base()


# =========================
# DEPENDENCY
# =========================
def get_db():
    db = SessionLocal()
    try:
        yield db
    except SQLAlchemyError as e:
        logger.error(f"DB Error: {str(e)}")
        db.rollback()
        raise
    finally:
        db.close()


# =========================
# HEALTH CHECK
# =========================
def check_db():
    try:
        db = SessionLocal()
        db.execute(text("SELECT 1"))   # SQLAlchemy 2.x safe
        db.close()
        logger.info("DB Connected ✅")
        return True
    except Exception as e:
        logger.error(f"DB connection failed: {str(e)}")
        return False