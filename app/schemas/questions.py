from datetime import datetime

from pydantic import BaseModel, Extra, Field, validator


class QuestionCount(BaseModel):
    questions_num: int = Field(...)


class Question(BaseModel):
    id: int
    text: str
    answer: str
    creation_date: datetime
