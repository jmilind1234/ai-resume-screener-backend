from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# URL is used to define the location of the database used in our project
SQLALCHEMY_DATABASE_URL = "postgresql://neondb_owner:npg_AFD3l6aPmoxM@ep-sparkling-brook-ai99ukx2-pooler.c-4.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

#engine is used to open connection to the database and work with it. Engine holds the configuration.
engine = create_engine(SQLALCHEMY_DATABASE_URL)

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#sessionLocal is basically the factory to create the database session.Database session is used to interact with the database.

Base = declarative_base()
# this is the base class which will be imported by other classes to create the models in python.
