from fastapi import APIRouter

from .endpoints import curso


api_router_v1 = APIRouter()
api_router_v1.include_router(curso.router, tags=['cursos'], prefix="/cursos")