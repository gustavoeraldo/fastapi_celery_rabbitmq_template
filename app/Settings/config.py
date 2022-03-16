from typing import Optional, List
from pydantic import AnyHttpUrl, BaseSettings, HttpUrl, PostgresDsn
from dotenv import find_dotenv, load_dotenv
import os

load_dotenv(find_dotenv())

_SECRET_KEY = os.getenv("SECRET_KEY")


class Settings(BaseSettings):
    API_PATH_VERSION: str = "/"
    SECRET_KEY: str = _SECRET_KEY
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    SERVER_HOST: Optional[AnyHttpUrl]
    SERVER_NAME: "API"
    SERVER_VERSION: os.getenv("SERVER_VERSION")

    # BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ORIGINS
    BACKEND_CORS_ORIGINS: List[str] = os.getenv("ORIGINS")

    PROJECT_NAME: str = "Rabbit + Celery + FastAPI"
    SENTRY_DNS: Optional[HttpUrl] = None

    # DATABASE [Primary]
    PRIMARY_DATABASE: Optional[PostgresDsn] = os.getenv("DATABASE_URL")

    # DATABASE [Secondary]
    SECONDARY_DATABASE: Optional[PostgresDsn] = os.getenv("DATABASE_2_URL")


    # RABBITMQ SETTINGS
    RABBITMQ_URL = os.getenv("RABBITMQ_URL")

    # CELERY SETTINGS
    CELERY_BACKEND = os.getenv("CELERY_BACKEND")


settings = Settings()
