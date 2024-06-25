from fastapi import FastAPI, Query, Depends
from typing import Optional
from pydantic import BaseModel
from app.users.router import router as router_users
from app.bookings.router import router as router_bookings


app = FastAPI()
app.include_router(router_users)
app.include_router(router_bookings)


class SBooking(BaseModel):
    room_id: int
    date_from: str
    date_to: str


class SHotel(BaseModel):
    addres: str
    name: str
    stars: int


class HotelsSearchArgs:
    def __init__(
        self,
        location: str,
        date_from: str,
        date_to: str,
        has_spa: Optional[bool] = None,
        stars: Optional[int] = Query(None, ge=1, le=5),
    ) -> None:
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.has_spa = has_spa
        self.stars = stars


@app.get("/hotels")
async def get_hotels(search_args: HotelsSearchArgs = Depends()):
    return search_args


@app.post("/booking")
async def booking(booking: SBooking):
    return booking
