from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class UserCreate(BaseModel):
    id: UUID | None = Field(default_factory=uuid4)
    name: str
    email: str
    is_active: bool | None = True
    is_superuser: bool | None = False


class UserRead(BaseModel):
    id: UUID
    name: str
    email: str
    is_active: bool
    is_superuser: bool


class UserUpdate(BaseModel):
    name: str | None = None
    email: str | None = None
    is_active: bool | None = None
    is_superuser: bool | None = None


# from uuid import UUID, uuid4

# from pydantic import BaseModel, Field, EmailStr, SecretStr


# class UserBase(BaseModel):
#     username: str
#     email: EmailStr


# class UserRead(UserBase):
#     pass


# class UserCreate(UserBase):
#     id: UUID = Field(default_factory=uuid4)
#     password: SecretStr
#     is_superuser: bool | None = False
#     active_game_sessions: list[UUID] | None = Field(default_factory=list)


# class UserUpdate(UserBase):
#     username: str | None = None
#     email: EmailStr | None = None
#     password: SecretStr | None = None


# class UserInDB(UserBase):
#     id: UUID
#     hashed_password: SecretStr
#     is_superuser: bool
#     active_game_sessions: list[UUID]


# class UserGetDB(UserInDB):
#     pass
