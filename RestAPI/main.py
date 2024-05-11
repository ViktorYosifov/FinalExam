from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from sqlalchemy.orm import Session
from sqlite_database import SessionLocal, engine
import pydantic_models



app = FastAPI()


# #Dependancy
# def get_db():
#     db = SessionLocal()
#     try:
#         yield  db
#     finally:
#         db.close()

@app.post("/create_user", response_model=pydantic_models.ShowUser) #user already created -> response = ShowUser;
def create_user(user: pydantic_models.CreateUser):
    db = SessionLocal()
    new_user = pydantic_models.CreateUser(first_name=user.first_name,
                                          last_name=user.last_name,
                                          username=user.username,
                                          email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.post("/create_object")
def create_object(object: pydantic_models.CreateObject):
    pass

@app.post("/create_policy")
def create_policy(policy: pydantic_models.CreatePolicy):
    pass


@app.get("/show_users", response_model=pydantic_models.ShowUser)# include List from typing; response modela e list ot showuser;
def show_users(user: pydantic_models.ShowUser):
    db = SessionLocal()

@app.get("/show_objects")
def show_objects(object: pydantic_models.ShowObject):
    pass

@app.get("/show_policy")
def show_policy(policy: pydantic_models.ShowPolicy):
    pass


@app.delete("/delete_user")
def delete_user(user: pydantic_models.ShowUser):
    db = SessionLocal()

@app.delete("/delete_object")
def delete_object(object: pydantic_models.ShowObject):
    db = SessionLocal()

@app.delete("/delete_policy")
def delete_policy(policy: pydantic_models.ShowPolicy):
    pass

