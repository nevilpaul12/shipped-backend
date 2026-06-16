from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ARRAY, DateTime
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy.sql import func

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    created_at = Column(DateTime, server_default=func.now())

class DevLogs(Base):

    __tablename__ = "logs"

    #id should be auto incremented and primary key
    id = Column(Integer,primary_key=True,index=True,autoincrement=True)
    title = Column(String)
    description = Column(String)
    links = Column(MutableList.as_mutable(ARRAY(String)), default=list)
    images = Column(MutableList.as_mutable(ARRAY(String)), default=list)
    takeaway = Column(String)
    created_at = Column(DateTime, server_default=func.now())
