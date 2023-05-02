from typing import Optional

from fastapi_users import schemas
from pydantic import EmailStr


class UserRead(schemas.BaseUser[int]):
    id: int
    first_name: str
    surname: str
    email: EmailStr
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "first_name": "John",
                "surname": "Doe",
                "email": "JohnDoe@gmail.com",
                "is_active": True,
                "is_superuser": False,
                "is_verified": False,
            }
        }


class UserCreate(schemas.BaseUserCreate):
    first_name: str
    surname: str
    email: EmailStr
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False

    class Config:
        schema_extra = {
            "example": {
                "first_name": "John",
                "surname": "Doe",
                "email": "JohnDoe@gmail.com",
                "password": "12345678",
                "is_active": True,
                "is_superuser": False,
                "is_verified": False,
            }
        }


class UserUpdate(schemas.BaseUserUpdate):
    pass
