import logging
from functools import lru_cache
from typing import List

from decouple import config
from pydantic import BaseSettings

log = logging.getLogger("uvicorn")


class Setting(BaseSettings):
    APP_VERSION: str = config("APP_VERSION", default="0.0.1")
    APP_DESCRIPTION: str = config("APP_DESCRIPTION", default="API")
    APP_NAME: str = config("APP_NAME", default="FastApi Boilerplate")
    APP_PORT: int = config("APP_PORT", default=8000, cast=int)
    ENVIRONMENT: str = config("ENVIRONMENT", default="local")
    ROOT_PATH: str = config("ROOT_PATH", default="/")
    TESTING: bool = config("TESTING", default=False, cast=bool)
    EMAIL_ADMIN: str = config("EMAIL_ADMIN")
    PASSWORD_ADMIN: str = config("PASSWORD_ADMIN")
    DB_URL = config("DB_URL")
    DB_TEST_URL = config("DB_TEST_URL")
    GENERATE_SCHEMAS = config("GENERATE_SCHEMAS")
    FIRE_BASE_CONFIG = config("FIRE_BASE_CONFIG")
    ALLOW_HEADERS: List = ["*"]
    ALLOW_METHODS: List = ["*"]
    ORIGINS: List = ["*"]
    MODELS: List = [
        "aerich.models",
    ]


@lru_cache()
def get_settings():
    log.info("Loading Config Application.")
    return Setting()
