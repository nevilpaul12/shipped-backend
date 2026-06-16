from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

database_url = os.getenv("Database_URL")
engine = create_engine(database_url)
sessionLocal = sessionmaker(autoflush=False,bind=engine)