from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.questions import QuestionInDB


class DBManager:

    def __init__(self, model):
        self.model = model

    @staticmethod
    async def create_bulk(session: AsyncSession, income_objs: list[dict]):
        for obj in income_objs:
            new_question = QuestionInDB(
                id=obj.get('id'),
                text=obj.get('question'),
                answer=obj.get('answer'),
            )
            session.add(new_question)
        await session.commit()

    async def get_all_objects(self, session: AsyncSession):
        questions = await session.execute(select(self.model).order_by(self.model.creation_date.desc()))
        return questions.scalars().all()


manager = DBManager(QuestionInDB)
