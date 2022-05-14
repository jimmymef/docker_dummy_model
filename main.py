from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import constr, PositiveInt
import logging
import asyncio
import random
from datafuncs import Datafuncs
from enum import Enum

# Preparar el logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")

file_handler = logging.FileHandler("logs_dummy_model.log")
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)  # Se agrega handler para consola

app = FastAPI()

class Gender(str, Enum):
    male = "male"
    female = "female"
    undisclosed = "undisclosed"

class Data_Model(BaseModel):
    active: bool
    balance: float = 0
    email: EmailStr = None
    age: PositiveInt
    name: constr(min_length=4)
    gender: Gender

@app.get("/")
def hello():
    logger.info(f"App open and ready!")
    return "hola mundo!"

@app.post("/validate_data")
async def validate_data(data_: Data_Model):
    funx = Datafuncs()
    validation = funx.validate_data(data_)
    logger.info("New data validation")
    return {"message": "Data was validated. All Good!", "valid" : validation}

@app.post("/make_prediction")
async def make_prediction(data_: Data_Model):
    funx = Datafuncs()
    prediction_result = funx.make_prediction2(data_)
    logger.info(f"New prediction")
    return {"message":prediction_result, "prediction":True}

@app.get("/get_info")
async def get_info():
    logger.info(f"User asked for info")
    return {"message":"This API bla bla bla"}