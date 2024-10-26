from fastapi import FastAPI

app = FastAPI()

@app.get("/login") # decorator
async def get_user(): # async function
    return {"message": "Hello Priyanshu"} # return a dictionary

# The order of decorator matters if both has same paths defined
@app.get("/posts")
def get_post():
    return {"data": "This is your post"}