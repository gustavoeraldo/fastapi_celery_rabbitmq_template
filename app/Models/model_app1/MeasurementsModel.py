from sqlalchemy import Column, ForeignKey, Integer, DateTime, Float, String
from sqlalchemy.sql import func

from app.Database import Base1

class Measurements(Base1):
  __tablename__ = 'measurements'
  __bind_key__ = 'Base1'

  measure_id = Column(Integer, primary_key=True, index=True)
  type_id = Column(Integer, ForeignKey('value_types.m_type_id'), nullable=False)
  user_id = Column(Integer, ForeignKey('users.usr_id'), nullable=False)
  measure = Column(Float,nullable=False)
  tag = Column(String(20))
  created_at = Column(DateTime(timezone=True), default=func.now())
  deleted_at = Column(DateTime)