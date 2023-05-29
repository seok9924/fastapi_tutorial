from fastapi import FastAPI
from typing import Union

app = FastAPI()


@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item

#http://127.0.0.1:8000/items/foo-item
#uvicorn required_q:app --reload
#http://127.0.0.1:8000/items/foo-item?needy=sooooneedy

app2=FastAPI()


@app2.get("/items/{item_id}")
async def read_user_item(
    item_id: str, needy: str, skip: int = 0, limit: Union[int, None] = None
):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item


# needy, 필수적인 str.
# skip, 기본값이 0인 int.
# limit, 선택적인 int.