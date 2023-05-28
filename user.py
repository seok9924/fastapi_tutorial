from fastapi import FastAPI

app = FastAPI()


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

# 경로 동작은 순차 평가 이므로 위에 쓰는게 먼저 나온다
@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

#uvicorn user:app --reload
