"""Student model"""
from sqlalchemy import Column
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import relationship, mapper
from manage1.model import meta
from manage1.model import Base


class Users(Base):
    __tablename__ = "users"

    id = Column('uid', Integer, primary_key=True)
    email = Column('username', String(100))
    password = Column('password', String(100))


