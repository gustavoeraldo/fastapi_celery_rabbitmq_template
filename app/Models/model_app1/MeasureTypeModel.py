from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.Database import Base1

class MeasuresType(Base1):
  __tablename__ = 'value_types'
  __bind_key__ = 'Base1'

  m_type_id = Column(Integer, primary_key=True)
  description = Column(String(100), nullable=False)
  
  # Relationships
  measurements = relationship('Measurements')