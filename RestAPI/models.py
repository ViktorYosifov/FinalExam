from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    """
    Creating table with users which contains all users information, and
    it's relation to the other tables
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    policies = relationship("Policy", back_populates="user")

class Object(Base):
    """
    Creating table with objects that are basically a path, to which specified user
    has access
    """

    __tablename__ = "objects"

    id = Column(Integer, primary_key=True, index=True)
    path = Column(String, nullable=False)
    policies = relationship("Policy", back_populates="object")

class Policy(Base):

    
    """
    Creating table with policies -
    who will be able to access what
    """

    __tablename__ = "policies"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    object_id = Column(Integer, ForeignKey("object.id"), nullable=False)
    user = relationship("User", back_populates="policies")
    object = relationship("Object", back_populates="policies")

