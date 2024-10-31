from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from app.db import Base
from sqlalchemy.orm import relationship


class Cities(Base):
    __tablename__ = 'cities'
    city_id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    city_name = Column(String)
    country_id = Column(Integer, ForeignKey('countries.country_id'), nullable=False)
    latitude = Column(Numeric)
    longitude = Column(Numeric)

    country = relationship('Country', lazy='immediate', back_populates='cities_list')

    targets = relationship('Targets', lazy='immediate',back_populates='city')





    # # jobs = relationship('Job', lazy='immediate', back_populates='employee')
    # jobs = relationship('Job', back_populates='employee')
