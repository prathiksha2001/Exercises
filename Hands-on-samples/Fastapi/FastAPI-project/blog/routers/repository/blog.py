from sqlalchemy.orm import Session
from ... import models
from fastapi import status, HTTPException

def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create(request, db):
    new_blog = models.Blog(title=request.title, body = request.body, user_id = 2)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def get_blog(id, db):
    new_blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not new_blog:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail= f"{id} not found")
    return new_blog

def destroy(id, db):
    blog = db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog with id {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return "deleted"

def update_blog(request,id,db):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"id {id} not found")
    blog.update(request.dict())
    db.commit()
    return "updated"
