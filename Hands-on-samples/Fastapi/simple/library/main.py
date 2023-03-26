from fastapi import FastAPI, Depends, File,UploadFile
from . import schemas, models
from . database import engine,sessionLocal
from sqlalchemy.orm import Session
from typing import List
app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/')
def home(request : schemas.BookDetails , db: Session = Depends(get_db)):
    new_book = models.BookDetails(book_name = request.book_name,author=request.author,genre=request.genre)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

@app.get('/', response_model=List[schemas.BookDetails])
def index(db:Session = Depends(get_db)):
    result = db.query(models.BookDetails).all()
    return result

@app.delete('/delete/{id}')
def index(id:int,db:Session = Depends(get_db)):
    result = db.query(models.BookDetails).filter(id==id).first()
    db.delete(result)
    db.commit()
    return 'deleted'

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename }
