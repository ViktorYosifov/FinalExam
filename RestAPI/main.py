from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import List

from . import models, schemas, crud, database
from .logging_config import logger

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.database.connect()
    models.Base.metadata.create_all(bind=database.engine)

@app.on_event("shutdown")
async def shutdown():
    await database.database.disconnect()

async def get_db():
    async with Session(database.engine) as session:
        yield session

@app.post("/users/", response_model=schemas.CreateUser)
async def create_user(user: schemas.CreateUser, db: Session = Depends(get_db)):
    db_user = await crud.create_user(db, user)
    logger.info(f"User {user.username} created")
    return db_user

@app.delete("/users/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    policies = await crud.get_policies_by_user(db, user_id)
    if policies:
        raise HTTPException(status_code=400, detail="Cannot delete user whith existing policies")
    await crud.delete_user(db, user_id)
    logger.info(f"User {user_id} deleted")
    return JSONResponse(status_code=204)

@app.get("/users/", response_model=List[schemas.CreateUser])
async def list_users(db: Session = Depends(get_db)):
    return await crud.get_users(db)

@app.post("/objects/", response_model=schemas.CreateObject)
async def create_object(object: schemas.CreateObject, db: Session = Depends(get_db)):
    db_object = await crud.create_object(db, object)
    logger.info(f"Object {object.path} created")
    return db_object

@app.delete("/objects/{object_id}")
async def delete_object(object_id: int, db: Session = Depends(get_db)):
    policies = await crud.get_policies_by_object(db, object_id)
    if policies:
        await crud.delete_policy(db, policies)
        logger.info(f"Deleted policies related to object {object_id}")
    await crud.delete_object(db, object_id)
    logger.info(f"Object {object_id} deleted")
    return JSONResponse(status_code=204)

@app.get("/objects/", response_model=List[schemas.CreateObject])
async def list_objects(db: Session = Depends(get_db)):
    return await crud.get_objects(db)

@app.post("/policies/", response_model=schemas.CreatePolicy)
async def create_policy(policy: schemas.CreatePolicy, db: Session = Depends(get_db)):
    db_policy = await crud.create_policy(db, policy)
    logger.info(f"Policy created for user {policy.user_id} on object {policy.object_id}")
    return db_policy

@app.delete("/policies/{policy_id}")
async def delete_policy(policy_id: int, db: Session = Depends(get_db)):
    await crud.delete_policy(db, policy_id)
    logger.info(f"Policy {policy_id} deleted")
    return JSONResponse(status_code=204)

@app.get("/policies/user/{user_id}")
async def list_policies_by_user(user_id: int, db: Session = Depends(get_db)):
    return await crud.get_policies_by_user(db, user_id)

@app.get("/policies/object/{object_id}")
async def list_policies_by_object(object_id: int, db: Session = Depends(get_db)):
    return await crud.get_policies_by_object(db, object_id)
