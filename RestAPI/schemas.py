from pydantic import BaseModel, EmailStr

class CreateUser(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: EmailStr

class CreateObject(BaseModel):
    path: str

class CreatePolicy(BaseModel):
    user_id: int
    object_id: int


