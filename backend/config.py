from functools import lru_cache
from typing import List
from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    # APP CONFIG
    APP_NAME: str = "Cricket AI Backend"
    VERSION: str = "1.0.0"
    DEBUG: bool = True

    # SERVER CONFIG
    HOST: str = "127.0.0.1"
    PORT: int = 8000

    # SECURITY CONFIG
    SECRET_KEY: str = "supersecretkey123"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 120

    # DATABASE CONFIG  ✅ FIXED
    DATABASE_URL: str = "sqlite:///./cricket.db"

    # CORS CONFIG
    ALLOWED_ORIGINS: List[str] = ["*"]
    ALLOWED_METHODS: List[str] = ["*"]
    ALLOWED_HEADERS: List[str] = ["*"]

    # SCRAPING CONFIG
    USER_AGENT: str = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    SCRAPE_RETRIES: int = 3

    # FEATURE FLAGS
    ENABLE_CHAT: bool = True
    ENABLE_INSIGHTS: bool = True
    ENABLE_KNOWLEDGE: bool = True
    ENABLE_EXTERNAL: bool = True

    # Pydantic v2 config
    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "extra": "ignore"
    }

    # HELPERS
    def is_dev(self) -> bool:
        return self.DEBUG

    def get_database_url(self) -> str:
        return self.DATABASE_URL

    def get_cors_config(self):
        return {
            "origins": self.ALLOWED_ORIGINS,
            "methods": self.ALLOWED_METHODS,
            "headers": self.ALLOWED_HEADERS,
        }


# SINGLETON (IMPORTANT)
@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()