import logging

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.core.exceptions import APIStatusNotExpected
from app.services.collector import QuestionCollector
from app.services.crud import manager


logger = logging.getLogger(__name__)


async def get_and_save_questions(
        session: AsyncSession,
        questions_db,
        count: int,
):
    collector = QuestionCollector(settings.question_api_url)
    intersections_counter = 0
    try:
        questions_api = await collector.get_questions_from_api(count)
        validated_questions = await validate_existing_by_id(
            questions_api,
            questions_db,
        )
        while len(validated_questions) < count:
            if intersections_counter >= int(settings.intersections_maximum):
                logger.warning('Too many intersections by ID, '
                               'probably all questions are already in DB')
                break
            questions_api = await collector.get_questions_from_api(
                count - len(validated_questions),
            )
            validated_questions += questions_api
            validated_questions = await validate_existing_by_id(
                questions_api,
                questions_db,
            )
            intersections_counter += 1
        await manager.create_bulk(session, validated_questions)
    except APIStatusNotExpected as e:
        logger.error(f'Questions was not taken from API. Error: {e.args}')
    except Exception as e:
        logger.error(f'Something gone wrong. Error: {e.args}')


async def validate_existing_by_id(from_api, from_db) -> list[dict]:
    existing_ids = []
    for question in from_db:
        existing_ids.append(question.id)
    result = []
    for question in from_api:
        if question.get('id') not in existing_ids:
            result.append(question)
        else:
            logger.warning('ID Intersection found')
    return result
