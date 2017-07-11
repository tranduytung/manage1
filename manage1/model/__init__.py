"""The application's model objects"""
from manage1.model.meta import Session, Base
from manage1.model.student import Student
from manage1.model.course import Course


def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    Session.configure(bind=engine)
