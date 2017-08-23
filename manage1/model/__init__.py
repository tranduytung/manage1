"""The application's model objects"""
from manage1.model.meta import Session, Base
# from manage1.model.student import Student
from manage1.model.course import Course
from manage1.model.users import Users
from manage1.model.users_info import UsersInfo
from manage1.model.course_schedule import CourseSchedule
from manage1.model.course_schedule import ScheduleType
from manage1.model.activity import ActionType
from manage1.model.activity import Activity
from manage1.model.activity import ObjectType
from manage1.model.notification import Notification
import meta
import sqlalchemy as sa
# from sqlalchemy import orm
# from sqlalchemy import Column
# from sqlalchemy.types import Integer, String

def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    meta.Session.configure(bind=engine)
    meta.engine = engine

association_table = sa.Table('association', Base.metadata,
    sa.Column('user_id', sa.types.Integer, sa.ForeignKey('users.uid')),
    sa.Column('course_id', sa.types.Integer, sa.ForeignKey('course.id'))
)
# class Register(object):
#     user_id = Column('user_id', Integer)
#     course_id = Column('course_id', Integer)
# orm.mapper(Register, association_table)