from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class Blog(BaseModel):
    title: str
    body: str
    pulished : bool = False

@app.get("/blogs")
def index(limit : int = 10, publish: bool = True):
    if publish:
        return {"data":f"{limit} published blog from db"}
    else:
        return {"data":f"{limit} blog from db"}

@app.get("/blogs/{id}")
def show(id: int):
    return {"data": id}

@app.post("/blog")
def create_blog(blog : Blog):
    return blog
 