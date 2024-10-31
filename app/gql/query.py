from graphene import ObjectType, List, Field, Int, Date, String
from graphql import GraphQLError

from app.db.database import session_maker
from app.db.models import missions
from app.db.models.cities import Cities
from app.db.models.countries import Countries
from app.db.models.missions import Missions
from app.db.models.targets import Targets
from app.gql.types.missions_type import MissionsType


class Query(ObjectType):
    all_missions = List(MissionsType)
    missions_by_id = Field(MissionsType, mission_id=Int(required=True))
    missions_by_date_range = List(MissionsType, start=Date(required=True), end=Date(required=True))
    missions_by_country = List(MissionsType, country_name=String(required=True))

    @staticmethod
    def resolve_all_missions(root, info):
        with session_maker() as session:
            return session.query(Missions).all()

    @staticmethod
    def resolve_missions_by_id(root, info, mission_id):
        with session_maker() as session:
            return session.query(Missions).get(mission_id)

    @staticmethod
    def resolve_missions_by_date_range(root, info, start, end):
        with (session_maker() as session):
            return session.query(Missions).filter(Missions.mission_date.between(start, end)).all()

    @staticmethod
    def resolve_missions_by_country(root, info, country_name):
        with session_maker() as session:
            return session.query(Missions).join(Targets).join(Cities).join(Countries).filter(Countries.name == country_name).all()





    # @staticmethod
    # def resolve_all_employees(root, info):
    #     with session_maker() as session:
    #         return session.query(Employee).all()
    #
    # @staticmethod
    # def resolve_employees_by_id(root, info, employee_id):
    #     with session_maker() as session:
    #         employee =  (session.query(Employee)
    #                 .filter(Employee.id == employee_id)
    #                 .first())
    #         if not employee:
    #             raise GraphQLError('Employee not found')
    #         return employee
    #
    # @staticmethod
    # def resolve_all_jobs(root, info):
    #     with session_maker() as session:
    #         return session.query(Job).all()