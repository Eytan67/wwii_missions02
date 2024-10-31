from sqlalchemy import Column, Integer, String, Numeric
from app.db import Base
from sqlalchemy.orm import relationship


class Targets(Base):
    __tablename__ = 'targets'
    target_id = Column(Integer, nullable=False, autoincrement=True)
    mission_id = Column(Integer)
    target_industry = Column(String, nullable=False)
    city_id = Column(Integer)
    target_type_id = Column(Integer)
    target_priority = Column(Integer)