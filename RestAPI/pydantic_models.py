from pydantic import BaseModel

class CreateUser(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: str

class ShowUser(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str
    email: str

class CreateObject(BaseModel):
    path: str

class ShowObject(BaseModel):
    id: int
    path: str

class CreatePolicy(BaseModel):
    user_id: int
    object_id: int

class ShowPolicy(BaseModel):
    id: int
    user_id: int
    object_id: int

