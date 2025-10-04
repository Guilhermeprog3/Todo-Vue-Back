from pydantic import BaseModel, validator
from typing import Optional
from datetime import datetime

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: Optional[datetime] = None

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    completed: bool
    owner_id: int
    status: str

    class Config:
        from_attributes = True


class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

    @validator('password')
    def password_must_not_exceed_72_chars(cls, v):
        if len(v.encode('utf-8')) > 72:
            raise ValueError('A senha não pode ter mais de 72 caracteres.')
        return v

class User(UserBase):
    id: int
    tasks: list[Task] = []

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None