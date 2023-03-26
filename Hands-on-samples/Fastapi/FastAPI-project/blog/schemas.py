from pydantic import BaseModel
from typing import List, Union

class BaseBlog(BaseModel):
    title : str
    body : str

class Blog(BaseBlog):
    class Config():
        orm_mode = True

class BaseUser(BaseModel):
    name : str
    email : str
    password : str

class User(BaseModel):
    name : str
    email : str 
    
    class Config():
        orm_mode = True

class ShowUser(User):
    blogs : List[Blog]
    class Config():
        orm_mode = True
        

class ShowBlog(BaseBlog):
    creator : User
    class Config():
        orm_mode = True

class Login(BaseModel):
    username : str
    password : str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Union[str, None] = None
   
