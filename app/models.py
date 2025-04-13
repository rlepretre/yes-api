from pydantic import EmailStr
from sqlmodel import Field, SQLModel


# Shared properties
class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    email: EmailStr = Field(unique=True, index=True, max_length=255)
    full_name: str | None = Field(default=None, max_length=255)
    hashed_password: str | None = Field(default=None, min_length=8, max_length=255)


# Shared properties
class Thing(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(min_length=1, max_length=255)
    points: int


# Generic message
class Message(SQLModel):
    message: str


# JSON payload containing access token
class Token(SQLModel):
    access_token: str
    token_type: str = "bearer"


# Contents of JWT token
class TokenPayload(SQLModel):
    sub: str | None = None


class NewPassword(SQLModel):
    token: str
    new_password: str = Field(min_length=8, max_length=40)
