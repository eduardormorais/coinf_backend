from loguru import logger

from app.config.bootstrap import create_app
from app.config.db import close_connection_database, connect_to_database
from app.config.firebase import init_firebase

firebase = init_firebase()
app = create_app()


@app.on_event("startup")
async def statup_event():
    logger.info("Starting up...")

    await connect_to_database()


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down...")
    await close_connection_database()
