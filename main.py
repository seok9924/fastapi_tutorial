from fastapi import FastAPI

app = FastAPI()


@app.get("/") # post get put delete CRUD
async def root(): # 동기 비동기 처리 부분
    return {"message": "Hello World"}

#uvicorn main:app --reload
