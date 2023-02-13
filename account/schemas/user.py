from datetime import datetime
from pydantic import BaseModel, EmailStr, constr


class UserBaseSchema(BaseModel):
    name: str | None = None
    username: str
    email: str 
    type: str | None = None
    createdAt: datetime | None = None
    updatedAt: datetime | None = None

class CreateUserSchema(UserBaseSchema):
    password: constr(min_length=8)


class LoginUserSchema(BaseModel):
    email: EmailStr
    password: constr(min_length=8)


class UserResponseSchema(UserBaseSchema):
    id: str
    pass


class UserResponse(BaseModel):
    status: str
    user: UserResponseSchema

