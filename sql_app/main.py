from xml.sax import default_parser_list
from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/blog", response_model=schemas.Blog)
def create_blog(blog: schemas.BlogCreate, db: Session = Depends(get_db)):
    db_blog = crud.get_blog_by_email(db, email=blog.email)
    if db_blog:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered TST")
    return crud.create_blog(db=db, blog=blog)

@app.get("/blog", response_model=list[schemas.Blog])
def read_blogs(skip: int=0, limit: int=100, db: Session = Depends(get_db)):
    blogs = crud.get_blogs(db, skip=skip, limit=limit)
    return blogs

@app.get("/blog/{blog_id}", response_model=schemas.Blog)
def read_blog(blog_id: int, db: Session = Depends(get_db)):
    db_blog = crud.get_blog(db, blog_id=blog_id)
    if db_blog is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found TST")
    return db_blog

@app.post("/blog/{blog_id}/items", response_model=schemas.Item)
def create_item_for_blog(
    blog_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    db_blog = crud.get_blog(db, blog_id)
    if db_blog is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with {blog_id} blog id wasn`t found")
    return crud.create_blog_item(db=db, item=item, blog_id=blog_id)

@app.get("/items", response_model=list[schemas.Item])
def read_items(skip: int=0, limit: int=100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items

@app.get("/blog/{blog_id}/items", response_model=list[schemas.Item])
def read_item_for_blog(blog_id: int, db: Session = Depends(get_db)):
    db_blog = crud.get_blog(db, blog_id)
    if db_blog is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with {blog_id} blog id wasn`t found")
    return crud.get_item(db, blog_id)
