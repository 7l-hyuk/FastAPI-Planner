from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn
from .routes.events import event_router
from .routes.users import user_router

from src.database.connection import Settings


settings = Settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # TODO: Database initialize
    await settings.initialize_database()
    yield
    # TODO: Database clear

app = FastAPI(
    lifespan=lifespan
)

app.include_router(event_router)
app.include_router(user_router)


@app.get("/")
async def root_path():
    return "Hello, world!"


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
