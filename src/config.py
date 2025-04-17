from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str | None = None

    model_config = ConfigDict(
        env_file=".env"
    )


settings = Settings()
