from fastapi import  APIRouter

todo_router2=APIRouter()
todo_list=[]
# @todo_router2.post("/todo")
# async def add_todo(todo: dict)->dict:
#     todo_list.append(todo)
#     return {
#         "message":"Todo added"
#     }

@todo_router2.get("/todo")
async def retrieve_todos()->dict:
    return {
        "todos":todo_list
    }

#uvicorn todo_router:todo_router --reload
#APIRouter 클래스는 FastAPI 클래스와 동일한 방식으로 작동한다. 하지만 uvicorn은 APIROUTER() 인스턴스를 사용해서
#어플리케이션 실행 불가 APIRouter를 사용해 정의한 라우트를 FastAPI 인스턴스에 추가해야 외부에서 접근 가능
#include_router()
