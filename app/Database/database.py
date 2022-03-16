from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from typing import Generator
from fastapi import Request

from app.Settings.config import settings

DATABASE_1 = settings.PRIMARY_DATABASE
DATABASE_2 = settings.SECONDARY_DATABASE

engine1 = create_engine(DATABASE_1, pool_pre_ping=True, pool_size=3)
engine2 = create_engine(DATABASE_2, pool_pre_ping=True, pool_size=3)

Base1: DeclarativeMeta = declarative_base()
Base2: DeclarativeMeta = declarative_base()

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    binds={
        Base1: engine1,
        Base2: engine2,
    },
)


def get_db(request: Request) -> Generator:
    return request.state.db
