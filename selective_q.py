from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Union[str, None] = None):
    #Union[str, None]에 있는 Union은 FastAPI(FastAPI는 str 부분만 사용합니다)가 사용하는게 아니지만,
      # Union[str, None]은 편집기에게 코드에서 오류를 찾아낼 수 있게 도와줍니다.
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

#uvicorn selective_q:app --reload
