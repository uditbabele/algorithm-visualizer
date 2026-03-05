from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Submission(Base):

    __tablename__ = "submissions"

    id = Column(Integer, primary_key=True)
    user = Column(String)
    runtime = Column(Integer)
    memory = Column(Integer)