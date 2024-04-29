from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlite_database import Base

class User(Base):
    """
    Creating table with users which contains all users information, and
    it's relation to the other tables
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    username = Column(String)
    email = Column(String)
    policies = relationship("Policy", back_populates="user")

class Object(Base):
    """
    Creating table with objects that are basically a path, to which specified user
    has access
    """

    __tablename__ = "objects"

    id = Column(Integer, primary_key=True, index=True)
    path = Column(String)
    policies = relationship("Policy", back_populates="object")

class Policy(Base):
    """
    Creating table with policies -
    who will be able to access what
    """

    __tablename__ = "policies"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    object_id = Column(Integer, ForeignKey("object.id"))
    user = relationship("User", back_populates="policies")
    object = relationship("Object", back_populates="policies")

