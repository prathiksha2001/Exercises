from .database import Base
from sqlalchemy import Column, Integer, String

class BookDetails(Base):
    __tablename__ = 'booksss'
    id = Column(Integer, primary_key=True)
    book_name = Column(String, unique=True)
    author = Column(String, nullable=False)
    genre = Column(String, nullable=False)