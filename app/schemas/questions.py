from datetime import datetime

from pydantic import BaseModel, PositiveInt


class QuestionCount(BaseModel):
    questions_num: PositiveInt


class Question(BaseModel):
    id: int
    text: str
    answer: str
    creation_date: datetime
