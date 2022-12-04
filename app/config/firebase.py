import json
import os

from firebase import Firebase

from app.config.settings import get_settings
from loguru import logger

setting = get_settings()


def init_firebase() -> Firebase:
    logger.info("Configurando Firebase")

    def load_config_firebase() -> dict:
        config = None
        with open(setting.FIRE_BASE_CONFIG, "r") as file:
            config = json.loads(file.read())
        return config

    firebase = Firebase(load_config_firebase())
    logger.info("Firebase configurado.")
    return firebase
