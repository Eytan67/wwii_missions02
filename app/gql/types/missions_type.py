from graphene import ObjectType, Int, String, List, Date, Float, Decimal
from sqlalchemy import Numeric

from app.db.database import session_maker


class MissionsType(ObjectType):
    mission_id = Int()
    mission_date = Date()
    airborne_aircraft = Decimal()
    attacking_aircraft = Decimal()
    bombing_aircraft = Decimal()
    aircraft_returned = Decimal()
    aircraft_failed = Decimal()
    aircraft_damaged = Decimal()
    aircraft_lost = Decimal()

    # targets = List("app.gql.types.targets_type.TargetsType")
    # targets = List("app.gql.types.targets_type.TargetType")

    # @staticmethod
    # def resolve_jobs(root, info):
    #     with session_maker() as session:
    #         return (session.query(Job)
    #                 .filter(Job.employee_id == root.id)
    #                 .all())




