from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pymongo import MongoClient

# ---------------------------------------------------------
# PRIMARY DATABASE: PostgreSQL (Structured Relational Data)
# ---------------------------------------------------------
PG_URL = "postgresql://postgres:password@localhost:5432/wildlife_db"

pg_engine = create_engine(PG_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=pg_engine)
Base = declarative_base()

def get_pg_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ---------------------------------------------------------
# SECONDARY DATABASE: MongoDB (Unstructured / Sensor Data)
# ---------------------------------------------------------
MONGO_URL = "mongodb://localhost:27017"
mongo_client = MongoClient(MONGO_URL)
mongo_db = mongo_client["wildlife_metadata"]

def get_mongo_db():
    return mongo_db