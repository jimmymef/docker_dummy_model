from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import constr, PositiveInt
import logging
import asyncio
import random
from enum import Enum

# Preparar el logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")

file_handler = logging.FileHandler("logs_dummy_model_debug.log")
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)  # Se agrega handler para consola

class Datafuncs:
    def __init__(self) -> None:
        pass

    def validate_data(self, data_:any):
        logger.debug("New data validation")
        valid = True
        return (valid)
    
    def make_prediction2(self, data_:any):
        predictions_list = ["very good customer", "good customer", "average customer", "bad customer"]
        prediction_result = random.choice(predictions_list)
        logger.debug(f"New prediction: {prediction_result}")
        return (prediction_result)