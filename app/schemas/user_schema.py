from pydantic import BaseModel, EmailStr
from datetime import datetime,date
from typing import Optional


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    primary_mobile: str
    secondary_mobile: Optional[str] = None
    aadhaar: str
    pan: str
    date_of_birth: date
    place_of_birth: str
    current_address: str
    permanent_address: str


class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    primary_mobile: Optional[str] = None
    secondary_mobile: Optional[str] = None
    aadhaar: Optional[str] = None
    pan: Optional[str] = None
    date_of_birth: Optional[date] = None
    place_of_birth: Optional[str] = None
    current_address: Optional[str] = None
    permanent_address: Optional[str] = None


class UserResponse(BaseModel):
    id: str
    name: str
    email: EmailStr
    primary_mobile: str
    secondary_mobile: Optional[str]
    aadhaar: str
    pan: str
    date_of_birth: date
    place_of_birth: str
    current_address: str
    permanent_address: str
    created_at: datetime
