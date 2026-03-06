import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def preprocess(df):
    df = df.copy()
    df["hour"] = df["timestamp"].dt.hour
    df["day"] = df["timestamp"].dt.dayofyear
    df["smoothed"] = df["kwh"].rolling(window=3).mean()
    return df

def train_model(df):
    evening = df[(df["hour"] >= 18) & (df["hour"] <= 22)]

    X = evening[["hour", "day"]]
    y = evening["kwh"]

    model = LinearRegression()
    model.fit(X, y)
    return model

def predict_peak(model, df):
    next_day = df["day"].max() + 1

    future = pd.DataFrame({
        "hour": [18,19,20,21,22],
        "day": [next_day]*5
    })

    predictions = model.predict(future)
    peak_hour = future.iloc[np.argmax(predictions)]["hour"]

    return int(peak_hour)