from db import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True) 
    login = Column(String, unique=True, index=True)
    password = Column(String)
    tasks = relationship("Tasks", back_populates="owner")

class Tasks(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    is_done = Column(Boolean, default=False) 
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("Users", back_populates="tasks")
