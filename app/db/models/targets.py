from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from app.db import Base
from sqlalchemy.orm import relationship


class Targets(Base):
    __tablename__ = 'targets'
    target_id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    mission_id = Column(Integer, ForeignKey('missions.mission_id'))
    target_industry = Column(String, nullable=False)
    city_id = Column(Integer, ForeignKey('cities.city_id'))
    target_type_id = Column(Integer, ForeignKey('targettypes.target_type_id'))
    target_priority = Column(Integer)


    targets_type = relationship('TargetTypes', lazy='immediate', back_populates='targets')
    mission = relationship('Missions', lazy='immediate',back_populates='targets')
    city = relationship('Cities', lazy='immediate', back_populates='targets')

