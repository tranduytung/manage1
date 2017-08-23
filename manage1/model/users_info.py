"""UsersInfo model"""
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer, String, Boolean
from sqlalchemy.orm import relationship, backref
from manage1.model.meta import Base


class UsersInfo(Base):
    __tablename__ = "user_info"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.uid'))
    name = Column(String(100))
    avatar = Column(String(100))
    # access_token = Column(String(100))
    delete = Column(Boolean)
    user = relationship("Users", backref=backref("user_info", uselist=False))

    def __init__(self, name='', avatar=''):
        self.name = name
        self.avatar = avatar
        self.delete = False

    def __repr__(self):
        return "<User_Info('%s')" % self.name

