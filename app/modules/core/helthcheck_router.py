from fastapi import APIRouter

router = APIRouter()


@router.get("/health-check", description="Router to check helth application")
async def helthcheck():
    return {"msg": "Application running"}
