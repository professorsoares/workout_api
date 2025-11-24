from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
#    DB_URL: str = Field(default='postgresql+asyncpg://workout:workout@localhost/workout')
    DB_URL: str = Field(default='postgresql+asyncpg://postgres:e296cd9f@localhost/workout')


settings = Settings()