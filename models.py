from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    things = relationship("Thing", back_populates="user")


class Thing(Base):
    __tablename__ = "things"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.timezone)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="things")
