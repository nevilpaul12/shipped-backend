import os
import secrets
from datetime import datetime, timedelta
from typing import Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jwt
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "fallback_secret_key_if_missing")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

# Single owner of this project. No multi-user / signup.
OWNER_USERNAME = os.getenv("OWNER_USERNAME", "nevilpaul")
OWNER_PASSWORD = os.getenv("OWNER_PASSWORD", "nevilshipped")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def authenticate_owner(username: str, password: str) -> bool:
    """Return True only for the single owner's credentials."""
    return secrets.compare_digest(username, OWNER_USERNAME) and secrets.compare_digest(
        password, OWNER_PASSWORD
    )

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
    except jwt.InvalidTokenError:
        raise credentials_exception
    if username != OWNER_USERNAME:
        raise credentials_exception
    return username
