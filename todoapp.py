from fastapi import FastAPI
from todo_router import  todo_router2

app=FastAPI()
@app.include_router(todo_router2)


@app.get("/")
async def root():
    return {"message":"hello world"}

#uvicorn todoapp:app --reload


