from fastapi import APIRouter

from src.api.endpoints import upload

api_router = APIRouter()

api_router.include_router(upload.router)
