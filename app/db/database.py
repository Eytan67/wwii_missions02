from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.setings.config import DB_URL
from app.db import Base


engine = create_engine(DB_URL)
session_maker = sessionmaker(bind=engine)




# def init_db():
#     Base.metadata.drop_all(bind=engine)
#     Base.metadata.create_all(bind=engine)
#     with session_maker() as session:
#         session.add_all(employee_data)
#         session.add_all(jobs_data)
#         session.commit()
# from app.db.models.job import Job
# from app.db.models.employee import Employee
