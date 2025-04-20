import os

from pydantic import Field
from pydantic_settings import BaseSettings

os.environ["API_URL"] = 'http://localhost:8000'


class Settings(BaseSettings):
    api_url: str = Field(default="")
    secret_key: str = Field(default="")

    class Config:
        env_file = ".env.example"


print(Settings().model_dump())
