"""Course model"""
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer, String, DateTime, Enum
from sqlalchemy.orm import relationship, backref
from manage1.model.meta import Base
import enum
import datetime

class ActionType(enum.Enum):
    CREATE = 0
    EDIT = 1
    DELETE = 2
    FOLLOW = 3
    UNFOLLOW = 4

class ObjectType(enum.Enum):
    USER = 0
    COURSE = 1

class Activity(Base):
    __tablename__ = "activity"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.uid'))
    action_type = Column(Enum(ActionType))
    object_id = Column(Integer)
    object_type = Column(Enum(ObjectType))
    created_at = Column(DateTime)

    def __init__(self, action_type=None, object_id=None, object_type=None):
        self.action_type = action_type
        self.object_id = object_id
        self.object_type = object_type
        self.created_at = datetime.datetime.now()

    def __repr__(self):
        return "<Activity('%s')" % self.action_type
