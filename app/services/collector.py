import aiohttp


class QuestionCollector:
    def __init__(self, url: str):
        self.url = url

    async def get_questions_from_api(self, count: int) -> list[dict]:
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url + str(count)) as response:
                # FIXME! сделать проверку статуса ответа. наверное поднять эксепшн и в логи им насрать
                json = await response.json()
                return json
