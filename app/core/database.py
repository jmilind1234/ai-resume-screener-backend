from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import dotenv_values

config = dotenv_values(".env")

#engine is used to open connection to the database and work with it. Engine holds the configuration.
engine = create_engine(config["SQLALCHEMY_DATABASE_URL"])

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#sessionLocal is basically the factory to create the database session.Database session is used to interact with the database.

Base = declarative_base()
# this is the base class which will be imported by other classes to create the models in python.
