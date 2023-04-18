import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import tensorflow as tf
from tensorflow.keras.models import load_model
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
from typing import List


app = FastAPI()


# class Prediction(BaseModel):
#     time_steps: int
#     data: list[list[float]]
class Data(BaseModel):
    data: List[List[float]]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

model = load_model("model.h5")


@app.post("/predict")
async def predict(data: Data):
    # convert the input data to a numpy array and reshape it
    x = np.array(data.data).reshape(-1, 32, 1)
    # make predictions using the model
    y_pred = model.predict(x)
    # return the predicted values
    return {"predictions": y_pred.tolist()}



if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
