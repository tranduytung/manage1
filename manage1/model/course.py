"""Course model"""
from sqlalchemy import Column
from sqlalchemy.types import Integer, String

from manage1.model.meta import Base


class Course(Base):
    __tablename__ = "course"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    number = Column(Integer)

    def __init__(self, name='', number=0):
        self.name = name
        self.number = number

    def __repr__(self):
        return "<Course('%s')" % self.name
