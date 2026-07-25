# app/schemas.py
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    role_id: int  # Tying into your RBAC system

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    role_id: int

    class Config:
        orm_mode = True  # Allows Pydantic to read SQLAlchemy models

class Token(BaseModel):
    access_token: str
    token_type: str