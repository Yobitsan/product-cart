from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "postgresql://postgres:ballsack2021@localhost:5432/fastapi1"
engine = create_engine(db_url)
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)