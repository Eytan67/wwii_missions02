from graphene import ObjectType, Int, String, List, Date, Float, Field
from sqlalchemy import Numeric

from app.db.database import session_maker


class TargetsType(ObjectType):
    target_id = Int()
    mission_id = Int()
    target_industry = String()
    city_id = Int()
    target_type_id = Int()
    target_priority = Int()

    # targets_type = Field("app.gql.types.targets_type.TargetType")
    #city = Field("app.gql.types.cities_type.CitiesType")

    # @staticmethod
    # def resolve_jobs(root, info):
    #     with session_maker() as session:
    #         return (session.query(Job)
    #                 .filter(Job.employee_id == root.id)
    #                 .all())










