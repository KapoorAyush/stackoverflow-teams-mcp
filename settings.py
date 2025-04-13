from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    baseUrl: str
    apiKey: str
