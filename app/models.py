from uuid import uuid4

from sqlalchemy.types import UUID, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class User(Base):
    __tablename__ = "users"

    uuid = mapped_column(UUID, primary_key=True, default=uuid4)
    username: Mapped[str] = mapped_column(String(length=200), unique=True)
    password: Mapped[str] = mapped_column(String(length=500))
