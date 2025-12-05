from fastapi import APIRouter

from api.v1.endpoints import tshirt


api_router = APIRouter()
api_router.include_router(tshirt.router, prefix='/tshirts', tags=['tshirts'])