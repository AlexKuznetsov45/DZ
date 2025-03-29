from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    user_email = Column(String(120))
    subject_id = Column(Integer, ForeignKey("subject.subject_id"))

    subjects = relationship("Subject", back_populates="users")


class Subject(Base):
    __tablename__ = "subject"

    subject_id = Column(Integer, primary_key=True)
    subject_title = Column(String(80))

    users = relationship("User", back_populates="subjects")


class Student(Base):
    __tablename__ = "student"

    user_id = Column(Integer, ForeignKey("users.user_id"), primary_key=True)
    level = Column(String(60))
    education_form = Column(String(60))
    subject_id = Column(Integer, ForeignKey("subject.subject_id"))

    users = relationship("User", backref="students")
    subjects = relationship("Subject", backref="students")


class GroupStudent(Base):
    __tablename__ = "group_student"

    user_id = Column(Integer, ForeignKey("users.user_id"), primary_key=True)
    group_id = Column(Integer, primary_key=True)

    users = relationship("User", backref="group_students")


class Teacher(Base):
    __tablename__ = "teacher"

    teacher_id = Column(Integer, primary_key=True)
    email = Column(String(120))
    group_id = Column(Integer)
