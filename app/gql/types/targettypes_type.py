from graphene import ObjectType, Int, String, List, Date, Float, Field
from sqlalchemy import Numeric

from app.db.database import session_maker


class TargetTypesType(ObjectType):
    target_type_id = Int()
    target_type_name = String()



