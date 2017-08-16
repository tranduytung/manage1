"""Course model"""
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer, String, DateTime
from sqlalchemy.orm import relationship, backref
from manage1.model.meta import Base

class \
        Course(Base):
    __tablename__ = "course"

    id = Column(Integer, primary_key=True)
    code = Column(String(10))
    name = Column(String(100))
    number = Column(Integer)

    def __init__(self, code='', name='', number=0):
        self.code = code
        self.name = name
        self.number = number

    def __repr__(self):
        return "<Course('%s')" % self.name
