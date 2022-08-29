from sqlalchemy.orm import Session
from . import models, schemas

def get_blog(db: Session, blog_id: int):
    return db.query(models.Blog).filter(models.Blog.id == blog_id).first()

def get_blog_by_email(db: Session, email: str):
    return db.query(models.Blog).filter(models.Blog.email == email).first()

def get_blogs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Blog).offset(skip).limit(limit).all()

def create_blog(db: Session, blog: schemas.BlogCreate):
    db_blog = models.Blog(email=blog.email)
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog

def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()

def get_item(db: Session, blog_id: int):
    return db.query(models.Item).filter(models.Item.owner_id == blog_id).all()

def create_blog_item(db: Session, item: schemas.ItemCreate, blog_id: int):
    db_item = models.Item(**item.dict(), owner_id = blog_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item