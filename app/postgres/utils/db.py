from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
<<<<<<< HEAD
from dotenv import load_dotenv
import os
load_dotenv()  # Carica le variabili da .env

class Settings:
    database_url: str = os.getenv("DATABASE_URL")
=======
from app.postgres.utils.settings_db import Settings
>>>>>>> 135df6f877a338c2e2bba8803058ac727086b935

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