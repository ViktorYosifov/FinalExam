from sqlalchemy.future import select
from sqlalchemy.orm import Session
from . import models,schemas

async def create_user(db: Session, user: schemas.CreateUser):
    db_user = models.User(
        first_name=user.first_name,
        last_name=user.last_name,
        username=user.username,
        email=user.email
    )
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

async def delete_user(db: Session, user_id: int):
    db_user = await db.get(models.User, user_id)
    if db_user:
        await db.delete(db_user)
        await db.commit()

async def get_users(db: Session):
    result = await db.execute((select(models.User)))
    return result.scalars().all()

async def create_object(db: Session, object: schemas.CreateObject):
    db_object = models.Object(path=object.path)
    db.add(db_object)
    await db.commit()
    await db.refresh(db_object)
    return db_object

async def delete_object(db: Session, object_id: int):
    db_object = await db.get(models.Object, object_id)
    if db_object:
        await db.delete(db_object)
        await db.commit()

async def get_objects(db: Session):
    result = await db.execute(select(models.Object))
    return result.scalars().all()

async def create_policy(db: Session, policy: schemas.CreatePolicy):
    db_policy = models.Policy(user_id=policy.user_id, object_id=policy.object_id)
    db.add(db_policy)
    await db.commit()
    await db.refresh(db_policy)
    return db_policy

async def delete_policy(db: Session, policy_id: int):
    db_policy = await db.get(models.Policy, policy_id)
    if db_policy:
        await db.delete(db_policy)
        await db.commit()

async def get_policies_by_user(db: Session, user_id: int):
    result = await db.execute(select(models.Policy).where(models.Policy.user_id == user_id))
    return result.scalars().all()

async def get_policies_by_object(db: Session, object_id: int):
    result = await db.execute(select(models.Policy).where(models.Policy.object_id == object_id))
    return result.scalars().all()
