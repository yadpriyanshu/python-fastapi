from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional



app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


@app.get("/login") # decorator
async def get_user(): # async function
    return {"message": "Hello Priyanshu"} # return a dictionary

# The order of decorator matters if both has same paths defined
@app.get("/posts")
def get_post():
    return {"data": "This is your post"}

# @app.post("/createposts")
# def create_post(payLoad: dict = Body(...)):
#     print(payLoad)
#     return{"new_post": f"title {payLoad['title']} content: {payLoad['content']}"}

@app.post("/createposts")
def create_post(post: Post):
    print(post)
    print(post.dict())
    return{"data": "post"}

# title str, content str