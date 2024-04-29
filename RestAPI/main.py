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

@app.post("/create_user", response_model=pydantic_models.CreateUser)
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

@app.get("/all_users_listed", response_model=pydantic_models.ShowUser)
def list_all_users(user: pydantic_models.ShowUser):
    db = SessionLocal()
    users = db.query(User).all()

