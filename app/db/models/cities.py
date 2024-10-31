from sqlalchemy import Column, Integer, String, Numeric
from app.db import Base
from sqlalchemy.orm import relationship


class Cities(Base):
    __tablename__ = 'cities'
    city_id = Column(Integer, nullable=False, autoincrement=True)
    city_name = Column(String)
    country_id = Column(Integer, nullable=False)
    latitude = Column(Numeric)
    longitude = Column(Numeric)

    # jobs = relationship('Job', lazy='immediate', back_populates='employee')
    jobs = relationship('Job', back_populates='employee')
