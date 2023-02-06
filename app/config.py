from pathlib import Path

from pydantic import BaseSettings

BASE_DIR = Path(__file__).parent.parent


class DatabaseConfig(BaseSettings):
    roles: set = {"admin", "base", "moderator"}

    database_port: int
    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_host: str
    postgres_hostname: str
    database_url: str

    class Config:
        env_file = BASE_DIR / '.env'


class JWTConfig(BaseSettings):
    secret_key: str
    jwt_algorithm: str
    access_token_expire: int  # minutes
    refresh_token_expire: int  # days

    class Config:
        env_file = BASE_DIR / '.env'


database_config = DatabaseConfig()
jwt_config = JWTConfig()
