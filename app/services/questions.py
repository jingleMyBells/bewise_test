from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.services.collector import QuestionCollector
from app.services.crud import manager


async def get_and_save_questions(session: AsyncSession, questions_db, count: int):
    collector = QuestionCollector(settings.question_api_url)
    questions_api = await collector.get_questions_from_api(count)
    validated_questions = await validate_existing_by_id(questions_api, questions_db)
    while len(validated_questions) < count:
        questions_api = await collector.get_questions_from_api(count - len(validated_questions))
        validated_questions += questions_api
        validated_questions = await validate_existing_by_id(questions_api, questions_db)
    await manager.create_bulk(session, validated_questions)


async def validate_existing_by_id(from_api, from_db) -> list[dict]:
    existing_ids = []
    for question in from_db:
        existing_ids.append(question.id)
    result = []
    for question in from_api:
        if question.get('id') not in existing_ids:
            result.append(question)
        else:
            print('Случилось пересечение')
    return result
