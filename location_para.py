from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}") # 경로를 이렇게 받으면 url 개꿀
# async def read_item(item_id): # get 바로가능
#     return {"item_id": item_id}
async def read_item(item_id: int): # 타입 지정하면 int값만 들어감 ㄷㄷ
    return {"item_id": item_id} #즉, 타입 선언을 하면 FastAPI는 자동으로 요청을 "파싱"합니다.

#uvicorn location_para:app --reload
