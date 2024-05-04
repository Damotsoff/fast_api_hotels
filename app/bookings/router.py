from fastapi import APIRouter
from app.bookings.dao import BookingsDao
from app.bookings.schemas import SBooking



router = APIRouter(prefix="/bookings", tags=["Бронирование"])


@router.get("",response_model=SBooking)
async def get_bookings():
    return await BookingsDao.fin_one_or_none(id=1)
