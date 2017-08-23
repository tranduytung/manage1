"""Course model"""
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer, String, DateTime, Enum, Boolean
from sqlalchemy.orm import relationship, backref
from manage1.model.meta import Base
import enum
import datetime

class Notification(Base):
    __tablename__ = "notification"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.uid'))
    activity_id = Column(Integer, ForeignKey('activity.id'))
    is_read = Column(Boolean)
    activity = relationship("Activity", backref=backref("notification", uselist=False))

    def __init__(self, activity_id=None, is_read=False):
        self.activity_id = activity_id
        self.is_read = is_read

    def __repr__(self):
        return "<Notification('%s')" % self.activity_id
