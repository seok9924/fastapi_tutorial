from fastapi import  APIRouter

router=APIRouter()

@router.get("/hello")
async def say_hello()->dict:
    return {
        "message":"Hello"
    }

#uvicorn api_router:router --reload
