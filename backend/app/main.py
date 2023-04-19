import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import tensorflow as tf
from tensorflow.keras.models import load_model
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
import pandas as pd
from typing import List
from datetime import datetime
import random


app = FastAPI()



class TrafficData(BaseModel):
    date: str
    junction: int

class TrafficData2(BaseModel):
    date: str

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
df = pd.read_csv("traffic.csv")

# convert the date column to datetime format
# df['DateTime'] = pd.to_datetime(df['DateTime'], format='%d-%m-%Y %H:%M:%S')

# filter the data based on date and junction
# date = '01-11-2015'
# junction = 'J1'



# @app.post("/predict")
# async def predict(data: Data):
#     # convert the input data to a numpy array and reshape it
#     x = np.array(data.data).reshape(-1, 32, 1)
#     # make predictions using the model
#     y_pred = model.predict(x)
#     # return the predicted values
#     return {"predictions": y_pred.tolist()}

# api to get traffic prediction 
@app.post("/predict_by_date")
def predict_traffic(dt: TrafficData):

    date = dt.date
    junction = dt.junction

        # check if the input date is present in the traffic data
    # if not df["DateTime"].str.contains(date).any():
    #     return {"error": "Date not found in traffic data"}
    
    # Filter the data based on date and junction_id
    filtered_df = df[(df['DateTime'] == date) & (df['Junction'] == junction)]
    
    # Extract the vehicles column
    vehicles = filtered_df['Vehicles'].values.tolist()
    
    # Ensure that the vehicles list is of length 32
    if len(vehicles) < 32:
        for i in range(32-len(vehicles)):
            vehicles.append(random.randint(9,40))

    
    # Make the prediction
    prediction = model.predict([vehicles])
    
    # Return the prediction
    return {"predictions": prediction.tolist()}



# predict cars for all junctions at a date
@app.post("/predict_all_junction")
def predict_traffic_junctions(dt: TrafficData2):

    date = dt.date

        # check if the input date is present in the traffic data
    # if not df["DateTime"].str.contains(date).any():
    #     return {"error": "Date not found in traffic data"}
    
    # Filter the data based on date and junction_id
    filtered_df = df[(df['DateTime'] == date)]
    
    # Extract the vehicles column
    vehicles = filtered_df['Vehicles'].values.tolist()
    
    # Ensure that the vehicles list is of length 32
    junction_values = []
    if len(vehicles) < 32:
        for i in range(4):
            vehicle_value = []
            for i in range(32-len(vehicles)):
                vehicle_value.append(random.randint(9,40))
            junction_values.append(vehicle_value)
        
    # return {"predictions": junction_values}
    # Make the prediction
    results = []
    for i in range(4):
        prediction = model.predict([junction_values[i]])
        results.append(prediction)
    results = np.array(results)
    
    # Return the prediction
    return {"predictions": results.tolist()}



# @app.post("/predict_date")
# async def predict_date(traffic_data: TrafficData):
#     date = traffic_data.date
#     junction = traffic_data.junction
#     date = date.strptime(date, "%Y-%m-%d %H:%M:%S")
#     df_filtered = df[(df["date"] == date) & (df["junction"] == junction)]
#     # df_filtered = df[(df['DateTime'].dt.date == pd.to_datetime(date, format='%Y-%m-%d %H:%M:%S').date()) & (df['Junction'] == junction)]
#     data = df_filtered.tail(6)[["Vehicles"]].to_numpy()
#     x = np.array(data).reshape(1, 6, 1)
#     y_pred = model.predict(x)
#     return {"predictions": y_pred.tolist()}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)
