from sqlalchemy import select
from app.bookings.models import Bookings
from app.database import async_session_maker
from app.dao.base import BaseDAO


class BookingsDao(BaseDAO):
    model = Bookings
