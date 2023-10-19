import asyncio
from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.schemas.questions import QuestionCount, Question
from app.services.crud import manager
from app.services.questions import get_and_save_questions


router = APIRouter()


@router.post('/', response_model=Question)
async def post_question_cnt(input_data: QuestionCount, session: AsyncSession = Depends(get_async_session)):
    all_questions = await manager.get_all_objects(session)
    asyncio.create_task(get_and_save_questions(session, all_questions, input_data.questions_num))
    return all_questions[0]
