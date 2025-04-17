from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie, Document

from src.utils.logger import logger
from src.models.events import Event
from src.models.users import User
from src.config import settings


async def initialize_database():
    try:
        client = AsyncIOMotorClient(settings.DATABASE_URL)  # Client Access
        await init_beanie(
            database=client.get_default_database(),
            document_models=[Event, User]
        )
        logger.info("DATABASE CONNECTION SUCCESS")
    except Exception as e:
        logger.info(f"ERROR: {e}")


class Database:
    def __init__(self, model: Document):
        self.model = model

    async def save(self, document: Document):
        await document.create()
        return

    async def get_all(self):
        docs = await self.model.find_all().to_list()
        return docs

    async def get(self, id: int):
        doc = await self.model.get(id)
        return doc

    async def delete(self, id: int):
        doc = await self.get(id)
        await doc.delete()

    async def update(self, id: int, body):
        doc = await self.get(id)
        await doc.update(body)
