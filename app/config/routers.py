from fastapi import FastAPI
from fastapi_pagination import add_pagination


def init_routers(app: FastAPI):
    """
    This function is to load all routers in application.
    Here you can add routers from your modules.
    :param app:
    :return:
    """
    from app.modules.core import helthcheck_router
    from app.modules.pages import router as page_router
    from app.modules.images import router as image_router

    app.include_router(helthcheck_router.router)
    app.include_router(page_router.router, prefix="/page", tags=["Pages"])
    app.include_router(image_router.router, prefix="/image", tags=["Images"])

    add_pagination(app)
