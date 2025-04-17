from pydantic import ConfigDict
from pydantic_settings import BaseSettings
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie, Document

from src.logger import logger
from src.models.events import Event
from src.models.users import User


class Settings(BaseSettings):
    DATABASE_URL: str | None = None

    async def initialize_database(self):
        try:
            client = AsyncIOMotorClient(self.DATABASE_URL)  # Client Access
            await init_beanie(
                database=client.get_default_database(),
                document_models=[Event, User]
            )
            logger.info("database connection success")
        except Exception as e:
            logger.info(f"{e}")

    model_config = ConfigDict(
        env_file='.env'
    )


class Database:
    def __init__(self, model: Document):
        self.model = model

    async def save(self, document: Document):
        await document.create()
        return
    
    async def get_all(self):
        docs = await self.model.find_all().to_list()
        return docs
    

    
