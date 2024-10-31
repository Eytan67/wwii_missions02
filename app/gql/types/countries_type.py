from graphene import ObjectType, Int, String, List, Date, Float, Field
from sqlalchemy import Numeric

from app.db.database import session_maker


class CountriesType(ObjectType):
    country_id = Int()
    country_name = String()
