from graphene import ObjectType, Int, String, List, Date, Float, Field
from sqlalchemy import Numeric

from app.db.database import session_maker


class CitiesType(ObjectType):
    city_id = Int()
    city_name = String()
    country_id = Int()
    latitude = Float()
    longitude = Float


    # country = Field('"app.gql.types.countries_type.CountriesType"')

    # @staticmethod
    # def resolve_jobs(root, info):
    #     with session_maker() as session:
    #         return (session.query(Job)
    #                 .filter(Job.employee_id == root.id)
    #                 .all())


