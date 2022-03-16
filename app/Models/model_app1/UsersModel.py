from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.Database import Base1

class Users(Base1):
  __tablename__ = 'users'
  __bind_key__ = 'Base1'

  usr_id = Column(Integer, primary_key=True, index=True)
  username = Column(String(60), index=True, nullable=False)

  measurements = relationship('Measurements')