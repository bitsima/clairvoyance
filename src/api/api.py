from fastapi import APIRouter

from api.endpoints import upload

api_router = APIRouter()

api_router.include_router(upload.router, prefix="/api/v1")
