from fastapi import APIRouter, Depends,status, HTTPException
from .. import models, schemas
from ..database import get_db
from ..hashing import Hash
from sqlalchemy.orm import Session
from .repository import user 

router = APIRouter(prefix="/user" , tags=['Users'])

@router.post("/", response_model = schemas.ShowUser)
def create_user(request: schemas.BaseUser, db : Session = Depends(get_db)):
    return user.create(request,db)

@router.get("/{id}", response_model=schemas.ShowUser)
def get_user(id: int , db : Session = Depends(get_db)):
    return user.show(id,db)

@router.delete("/{id}")
def delete_user(id: int, db : Session = Depends(get_db)):
    return user.destroy(id,db)