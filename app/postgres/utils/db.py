from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.postgres.utils.settings_db import Settings

setting = Settings()
DATABASE_URL = setting.database_url

if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable must be set for PostgreSQL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autoflush=False, autocommit= False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()