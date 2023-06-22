from dotenv import find_dotenv
from pydantic import BaseSettings


class Settings(BaseSettings):
    telegram_token: str

    class Config:
        env_file = find_dotenv()
        env_file_encoding = 'utf-8'


settings = Settings()
