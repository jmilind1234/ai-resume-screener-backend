from pydantic import BaseModel, Field, EmailStr

class UserModel(BaseModel):
    email: EmailStr = Field(description="User email address")
    password: str = Field(description="User password", min_length=8)
