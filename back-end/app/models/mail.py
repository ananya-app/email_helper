# imports
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# database details
class MailDetails(Base):

    __tablename__ = "meetings"

    id = Column(Integer, primary_key=True,index=True)
    mailto = Column(String(256), index=True)
    subject = Column(String(256))
    text = Column(String())