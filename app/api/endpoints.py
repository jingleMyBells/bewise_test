import asyncio
import logging

from typing import Union

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.schemas.questions import QuestionCount, Question
from app.services.crud import manager
from app.services.questions import get_and_save_questions


logger = logging.getLogger(__name__)

router = APIRouter()


@router.post('/', response_model=Union[Question, list])
async def post_question_cnt(
        input_data: QuestionCount,
        session: AsyncSession = Depends(get_async_session),
):
    logger.info(f'Request arrived, question num: {input_data.questions_num}')
    all_questions = await manager.get_all_objects(session)
    asyncio.create_task(
        get_and_save_questions(
            session,
            all_questions,
            input_data.questions_num,
        )
    )
    if len(all_questions) == 0:
        return []
    return all_questions[0]
