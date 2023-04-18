import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import tensorflow as tf
from tensorflow.keras.models import load_model
from fastapi.middleware.cors import CORSMiddleware
import numpy as np


app = FastAPI()


class Prediction(BaseModel):
    time_steps: int
    data: list[list[float]]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.on_event("startup")
def load_model():
    global model
    # Load the saved model
    model = load_model("../model.h5")


@app.post("/predict")
async def predict_traffic(p: Prediction):
    # Transform the input data to numpy array
    data = np.array(p.data)

    # Reshape the data for input to the model
    data = np.reshape(data, (data.shape[0], p.time_steps, data.shape[1]))

    # Make the prediction using the loaded model
    pred = model.predict(data)

    # Convert the predicted values to a list
    pred_list = pred.tolist()

    # Return the predicted values
    return {"prediction": pred_list}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
