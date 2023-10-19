from fastapi import APIRouter

from app.api.endpoints import router as question_router


main_router = APIRouter()
main_router.include_router(
    question_router,
    prefix='/question',
    tags=['Questions']
)
