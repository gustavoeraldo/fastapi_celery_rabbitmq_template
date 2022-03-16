from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func

from app.Database import Base2

class Professionals(Base2):
    __tablename__ = 'professionals'
    __bind_key__ = 'Base2'

    id = Column(Integer, primary_key=True, index=True)
    cref = Column(String(11), unique=True, nullable=False)
    name = Column(String(40), nullable=False)
    phone = Column(String(14))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True))
    deleted_at = Column(DateTime(timezone=True))
