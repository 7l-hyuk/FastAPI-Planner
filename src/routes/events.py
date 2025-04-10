from fastapi import APIRouter
from src.models.events import Event

event_router = APIRouter(
    prefix="/events",
    tags=["Events"]
)

events: list[Event] = []


@event_router.get("/", response_model=list[Event])
async def get_all_events():
    return events


@event_router.get("/{id}", response_model=Event)
def get_event(id: int):
    for event in events:
        if event.id == id:
            return event
    return {"error": "Event not found"}


@event_router.post("/")
async def create_event(event: Event):
    events.append(event)
    return {"message": "Event created successfully"}


@event_router.put("/{id}")
async def update_event(id: int, event: Event):
    for i, event in enumerate(events):
        if event.id == id:
            events[i] = event
            return {"message": "Event updated successfully"}
    return {"message": "Event not found"}


@event_router.delete("/{id}")
async def delete_event(id: int):
    for event in events:
        if event.id == id:
            events.remove(event)
            return {"message": "Event deleted successfully"}
    return {"message": "Event not found"}
