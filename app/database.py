from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from app.config import database_config

engine = create_async_engine(url=database_config.database_url)

async_session = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    ...
