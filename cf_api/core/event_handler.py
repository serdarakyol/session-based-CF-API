from fastapi import FastAPI
from typing import Callable

from loguru import logger

from pathlib import Path
from pandas import read_pickle

ROOT_DIR = str(Path(__file__).parent.parent)

def start_app_handler(app: FastAPI) -> Callable:
    def startup() -> None:
        logger.info("Running app start handler.")
        app.state.data = read_pickle(ROOT_DIR + "/data/all_data.pkl")
    
    return startup

def stop_app_handler(app: FastAPI) -> Callable:
    def shutdown() -> None:
        logger.info("Running app shutdown handler.")
        del app.state.data

    return shutdown
