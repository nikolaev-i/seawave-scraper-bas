from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#we don't care about security since  this is local
engine = create_engine('postgresql://usr:pass@localhost:5432/bas')

Session = sessionmaker(bind=engine)

Base = declarative_base()