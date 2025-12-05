from typing import ClassVar
from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    """
    General configurations used in the applicattion.
    """

    API_VERSION: str = '/api/v1'
    DB_URL: str = "postgresql+asyncpg://michel:root@localhost:5432/catalog"
    DBBaseModel: ClassVar = declarative_base()

    class Config:
        case_sensitive = True


settings = Settings()