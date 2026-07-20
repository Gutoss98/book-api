from pydantic import BaseModel


class BookCreate(BaseModel):
    title: str
    author: str


class BookResponse(BookCreate):
    id: int

    model_config = {
        "from_attributes": True
    }
