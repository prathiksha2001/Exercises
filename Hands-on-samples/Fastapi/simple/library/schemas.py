from pydantic import BaseModel


class BookDetails(BaseModel):
    book_name : str
    author : str
    genre : str
    class Config():
        orm_mode = True