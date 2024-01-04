# imports
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# url for the database
SQLALCHEMY_DATABASE_URI = "sqlite:///./mails.sql"

engine = create_engine( 
    SQLALCHEMY_DATABASE_URI,
    # required for sqlite
    connect_args={"check_same_thread": False},
)
SessionLocal = sessionmaker(engine, autoflush=False)