from fastapi import APIRouter

event_router = APIRouter(
    prefix="/events",
    tags=["Events"]
)


@event_router.get("/")
async def get_all_events():
    return []


@event_router.get("/{id}")
def get_event():
    return ""


@event_router.post("/")
async def create_event():
    return ""


@event_router.put("/{id}")
async def update_event():
    return ""


@event_router.delete("/{id}")
async def delete_event():
    return ""
