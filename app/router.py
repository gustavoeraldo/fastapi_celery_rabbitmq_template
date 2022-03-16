from fastapi import APIRouter

from app.Endpoints import images

api_router = APIRouter()
api_router.include_router(images.router, prefix="/images", tags=["Images"])
