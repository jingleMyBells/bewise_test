import aiohttp
import logging

from app.core.exceptions import APIStatusNotExpected


logger = logging.getLogger(__name__)


class QuestionCollector:
    def __init__(self, url: str):
        self.url = url

    async def get_questions_from_api(self, count: int) -> list[dict]:
        logger.info('Trying to get questions from API')
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url + str(count)) as response:
                if response.status != 200:
                    raise APIStatusNotExpected('API response code is not 200')
                json = await response.json()
                logger.info('Got questions')
                return json
