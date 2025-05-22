from fastapi import APIRouter
from src.models.events import Event, EventUpdate
from src.database.connection import Database

event_router = APIRouter(
    prefix="/events",
    tags=["Events"]
)

event_db = Database(Event)


@event_router.get("/", response_model=list[Event])
async def get_all_events():
    events = await event_db.get_all()
    return events


@event_router.get("/{id}")
async def get_event(id: int):
    event = await event_db.get(id)
    return event


@event_router.post("/")
async def create_event(event: Event):
    await event_db.save(event)
    return {"message": "Event created successfully"}


@event_router.put("/{id}")
async def update_event(id: int, event: EventUpdate):
    await event_db.update(id, event)
    return {"message": "Event updated successfully"}


@event_router.delete("/{id}")
async def delete_event(id: int):
    await event_db.delete(id)
    return {"message": "Event deleted successfully"}
