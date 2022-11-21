from pydantic import BaseSettings


class Settings(BaseSettings):
    CORS_ORIGINS: str = "http://localhost"
    RABBITMQ_URL: str = "amqp://guest:guest@rabbit:5672/"


settings = Settings()
