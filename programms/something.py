import joblib
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from TaxiFareModel.predict import *
import pandas as pd
from datetime import datetime
import pytz



def get_model(path_to_joblib):
    pipeline = joblib.load(path_to_joblib)
    return pipeline



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.get("/predict")
def index(pickup_datetime, pickup_longitude, pickup_latitude,
          dropoff_longitude, dropoff_latitude, passenger_count):

    pickup_datetime = "2021-05-30 10:12:00"
    pickup_datetime = datetime.strptime(pickup_datetime, "%Y-%m-%d %H:%M:%S")

    # localize the user datetime with NYC timezone
    eastern = pytz.timezone("US/Eastern")
    localized_pickup_datetime = eastern.localize(pickup_datetime, is_dst=None)

    utc_pickup_datetime = localized_pickup_datetime.astimezone(pytz.utc)
    formatted_pickup_datetime = utc_pickup_datetime.strftime(
        "%Y-%m-%d %H:%M:%S UTC")

    X_pred = pd.DataFrame({
        'key':
        pd.Series(dtype='object'),
        'pickup_datetime':
        pd.Series(formatted_pickup_datetime, dtype='object'),
        'pickup_longitude':
        pd.Series(pickup_longitude, dtype='float64'),
        'pickup_latitude':
        pd.Series(pickup_latitude, dtype='float64'),
        'dropoff_longitude':
        pd.Series(dropoff_longitude, dtype='float64'),
        'dropoff_latitude':
        pd.Series(dropoff_latitude, dtype='float64'),
        'passenger_count':
        pd.Series(passenger_count, dtype='float64')
    })

    model = get_model('model.joblib')
    prediction = model.predict(X_pred)[0]

    return {"prediction": prediction}
