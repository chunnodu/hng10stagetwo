# Defining database models using SQLAlchemy
from sqlalchemy import Column, Integer, String
from db import Base


# Complete Person Schema (Pydantic Model)
class Person(Base):
    __tablename__ = "people"
    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(256))