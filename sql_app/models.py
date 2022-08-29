from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base

class Blog(Base):
    __tablename__ = "T_BLOGS"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique = True, index = True)
    is_active = Column(Boolean, default = True)

    items = relationship("Item", back_populates="owner")

class Item(Base):
    __tablename__ = "T_ITEMS"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("T_BLOGS.id"))

    #owner = relationship("Blog", back_populates="T_ITEMS")
    owner = relationship("Blog", back_populates="items")