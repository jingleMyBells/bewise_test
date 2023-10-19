from datetime import datetime

from sqlalchemy import Column, DateTime, Text

from app.core.db import Base


class QuestionInDB(Base):
    text = Column(Text, nullable=False)
    answer = Column(Text, nullable=False)
    creation_date = Column(DateTime, default=datetime.now)
