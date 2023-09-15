# Creates database engine and session

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# declare db url

DATABASE_URL = "sqlite:///./stagetwo.db"


# create sqlite engine instance

engine = create_engine(DATABASE_URL)

# create a DeclartiveMeta instance

Base = declarative_base()

# Create SessionLocal class from sessionmaker factory

SessionLocal = sessionmaker(expire_on_commit=False, bind=engine)
