from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
#db_url = "postgresql://postgres:ballsack2021@localhost:5432/fastapi1"
db_url=os.getenv("DATABASE_URL")
engine = create_engine(db_url)
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)