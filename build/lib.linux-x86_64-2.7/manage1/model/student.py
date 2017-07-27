# """Student model"""
# from sqlalchemy import Column, ForeignKey
# from sqlalchemy.types import Integer, String
# from sqlalchemy.orm import relationship, backref
# from manage1.model.meta import Base
# from authkit.users import Users
#
#
# class Student(Base):
#     __tablename__ = "student"
#
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey('users.uid'))
#     name = Column(String(100))
#     avatar = Column(String(100))
#
#     user = relationship("Users", backref=backref("student", uselist=False))
#     courses = relationship("Course",
#                            secondary='association',
#                            backref="students")
#
#     def __init__(self, name='', avatar=''):
#         self.name = name
#         self.avatar = avatar
#
#     def __repr__(self):
#         return "<Student('%s')" % self.name
#
