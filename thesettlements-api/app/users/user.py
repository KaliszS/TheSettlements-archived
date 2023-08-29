from pydantic import BaseModel, Field, EmailStr
from bson import ObjectId

from app.utils.mongo_utils import PyObjectId

class User(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    username: str
    email: EmailStr
    is_superuser: bool = False

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = { ObjectId: str }
        schema_extra = {
            "example": {
                "username": "Admin",
                "email": "testemail@mail.pl",
                "is_superuser": True,
            }
        }

class UserUpdate(BaseModel):
    username: str | None
    email: EmailStr | None
    is_superuser: bool | None

    class Config:
        schema_extra = {
            "example": {
                "username": "Admin",
                "email": "testemail@mail.pl",
                "is_superuser": True,
            }
        }

class UserCreate(User):
    password: str

    class Config:
        schema_extra = {
            "example": {
                "username": "Admin",
                "email": "testemail@mail.pl",
                "password": "password",
                "is_superuser": True,
            }
        }

class UserInDB(User):
    hashed_password: str

