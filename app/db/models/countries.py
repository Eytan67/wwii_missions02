from sqlalchemy import Column, Integer, String, Numeric
from app.db import Base
from sqlalchemy.orm import relationship


class Countries(Base):
    __tablename__ = 'countries'
    country_id = Column(Integer, nullable=False, primary_key=True,autoincrement=True)
    country_name = Column(String, nullable=False)

    cities_list = relationship('Cities', lazy='immediate', back_populates='country')