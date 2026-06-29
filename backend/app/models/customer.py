from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.database.database import Base

class Customer(Base):

    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(primary_key=True)

    first_name: Mapped[str] = mapped_column(String(50))

    last_name: Mapped[str] = mapped_column(String(50))

    phone: Mapped[str] = mapped_column(String(20))

    address: Mapped[str] = mapped_column(String(255))