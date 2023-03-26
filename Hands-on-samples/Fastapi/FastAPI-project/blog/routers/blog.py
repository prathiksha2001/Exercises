from fastapi import APIRouter, status, HTTPException, Depends
from ..database import SessionLocal, get_db
from typing import List
from sqlalchemy.orm import Session
from .. import models, schemas, oauth2
from .repository import blog


router = APIRouter(prefix = "/blog", tags=['Blogs'])

@router.post('/', status_code=status.HTTP_201_CREATED)
def create_blog(request : schemas.Blog, db:Session = Depends(get_db),current_user : schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request, db)
    
@router.get('/', response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)

@router.get('/{id}', response_model= schemas.ShowBlog)
def get_blog(id : int,db: Session = Depends(get_db),current_user : schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_blog(id,db)    
    

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db : Session = Depends(get_db),current_user : schemas.User = Depends(oauth2.get_current_user)):
    return  blog.destroy(id,db)

@router.put('/{id}', status_code=status.HTTP_200_OK)
def update_blog(request: schemas.Blog ,id: int, db : Session = Depends(get_db),current_user : schemas.User = Depends(oauth2.get_current_user)):
   return blog.update_blog(request,id,db)