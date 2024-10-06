from fastapi import FastAPI, Depends
import numpy as np
import pickle
import uvicorn
from pydantic_models import Day
from adapter import add_prediction
from db import get_session


with open("../data/weights.joblib", 'rb') as f:
    model = pickle.load(f)


app = FastAPI()


@app.get("/health")
async def get_health():
    return '', 200


@app.post("/request/")
async def model_request(day: Day) -> float:
    day_list = list(dict(day).values())
    day_array = np.array(day_list)
    result = model.predict(day_array.reshape(1, -1))
    result = round(result[0], 3)
    async for db in get_session():
        await add_prediction(db, dict(day), result)
    return {"result": result}

