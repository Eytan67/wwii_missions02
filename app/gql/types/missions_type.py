from graphene import ObjectType, Int, String, List, Date, Float
from sqlalchemy import Numeric

from app.db.database import session_maker


class MissionsType(ObjectType):
    mission_id = Int()
    mission_date = Date()
    airborne_aircraft = Float
    attacking_aircraft = Float
    bombing_aircraft = Float
    aircraft_returned = Float
    aircraft_failed = Float
    aircraft_damaged = Float
    aircraft_lost = Float


    # targets = List("app.gql.types.targets_type.TargetType")

    # @staticmethod
    # def resolve_jobs(root, info):
    #     with session_maker() as session:
    #         return (session.query(Job)
    #                 .filter(Job.employee_id == root.id)
    #                 .all())




