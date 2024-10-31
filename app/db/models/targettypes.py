from sqlalchemy import Column, Integer, String, Numeric
from app.db import Base
from sqlalchemy.orm import relationship


class TargetTypes(Base):
    __tablename__ = 'targettypes'
    target_type_id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    target_type_name = Column(String, nullable=False)

    targets = relationship('Targets', lazy='immediate', back_populates='targets_type')

