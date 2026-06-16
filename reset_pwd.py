import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import db_models
from auth import get_password_hash

database_url = "postgresql://nevil:123456@localhost:5432/weekly_devlogs"
engine = create_engine(database_url)
SessionLocal = sessionmaker(autoflush=False, bind=engine)
db = SessionLocal()

users = db.query(db_models.User).all()
if not users:
    print("No users found in the database.")
    sys.exit(0)

print(f"Found {len(users)} user(s).")
for user in users:
    print(f"Resetting password for user: {user.username}")
    user.hashed_password = get_password_hash("password123")
    
db.commit()
print("All passwords have been successfully reset to 'password123'")
