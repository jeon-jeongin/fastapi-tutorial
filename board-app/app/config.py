import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./board.db")
    DEBUG: bool = os.getenv("DEBUG", "true").lower() == "true"

    # JWT 설정
    SECRET_KEY: str = os.getenv("SECRET_KEY", "change-me-in-env")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

settings = Settings()