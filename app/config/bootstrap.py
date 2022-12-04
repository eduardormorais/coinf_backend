from fastapi import FastAPI
from loguru import logger

from app.config.jwt import exception_jwt, init_jwt
from app.config.middlewares import init_middlewares
from app.config.routers import init_routers
from app.config.settings import get_settings

setting = get_settings()
logger.info("Application is running")


def create_app() -> FastAPI:
    """This function is to initialize the application and all configurations."""
    application = FastAPI(
        title=setting.APP_NAME,
        version=setting.APP_VERSION,
        description=setting.APP_DESCRIPTION,
        root_path=setting.ROOT_PATH,
    )

    init_routers(application)
    init_middlewares(application)
    exception_jwt(application)
    init_jwt()
    return application
