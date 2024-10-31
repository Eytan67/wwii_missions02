from sqlalchemy import Column, Integer, String, Numeric, Date
from app.db import Base
from sqlalchemy.orm import relationship


class Missions(Base):
    __tablename__ = 'missions'
    mission_id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    mission_date = Column(Date)
    airborne_aircraft = Column(Numeric)
    attacking_aircraft = Column(Numeric)
    bombing_aircraft = Column(Numeric)
    aircraft_returned = Column(Numeric)
    aircraft_failed = Column(Numeric)
    aircraft_damaged = Column(Numeric)
    aircraft_lost = Column(Numeric)

    targets = relationship('Targets', lazy='immediate', back_populates='mission')

