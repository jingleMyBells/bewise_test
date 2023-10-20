from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_title: str = 'Тестовое задание Bewise,ai'
    app_description: str = ('Приложение для выдачи '
                            'случайных вопросов в викторине')
    secret: str = 'SNEAKY_SECRET'
    database_url: str = 'sqlite+aiosqlite:///./fastapi.db'
    question_api_url: str = 'https://jservice.io/api/random?count='
    intersections_maximum: int = 100

    model_config = SettingsConfigDict(env_file='.env')


settings = Settings()
