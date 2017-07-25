"""The application's model objects"""
from manage1.model.meta import Session, Base
from manage1.model.student import Student
from manage1.model.course import Course
from manage1.model.users import Users
import meta
import sqlalchemy as sa
from sqlalchemy import orm


def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    meta.Session.configure(bind=engine)
    meta.engine = engine

association_table = sa.Table('association', Base.metadata,
    sa.Column('student_id', sa.types.Integer, sa.ForeignKey('student.id')),
    sa.Column('course_id', sa.types.Integer, sa.ForeignKey('course.id'))
)
