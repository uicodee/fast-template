from fastapi import APIRouter

router = APIRouter(prefix="/test")


@router.get(path="/ping")
async def test_endpoint():
    return {"ping": "pong"}
