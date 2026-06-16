from pydantic import BaseModel
from datetime import datetime


class UserCreate(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    created_at: datetime | None = None

    class Config:
        from_attributes = True

class DevLogs(BaseModel):
    title: str
    description: str
    links: list[str] | None = None
    images: list[str] | None = None
    takeaway: str

class DevLogsResponse(DevLogs):
    id: int
    created_at: datetime | None = None

    class Config:
        from_attributes = True
