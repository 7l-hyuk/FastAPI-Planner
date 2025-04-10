from pydantic import ConfigDict
from beanie import Document


# Document Model
class Event(Document):
    id: int
    title: str
    image: str
    description: str
    tags: list[str]
    location: str
    created_at: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "id": 1,
                "title": "FastAPI planner",
                "image": "path/to",
                "description": "This is FastAPI planner tutorial",
                "tags": ["#FastAPI"],
                "location": "제 1 실습관 207호"
            }
        }
    )
