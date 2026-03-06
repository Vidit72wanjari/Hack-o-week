from flask import Flask
from flask_socketio import SocketIO
import os
import pickle
import random
import time
import threading
from datetime import datetime
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import urlopen

import pandas as pd

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

MODEL_PATH = Path(__file__).with_name("model.pkl")
model = pickle.load(open(MODEL_PATH, "rb"))


def _fetch_weather():
    """
    Fetch current temperature/humidity from OpenWeather.
    Falls back to None if no API key or any error occurs.
    """
    api_key = os.environ.get("OPENWEATHER_API_KEY")
    city = os.environ.get("WEATHER_CITY", "Delhi,IN")
    units = "metric"

    if not api_key:
        return None

    try:
        qs = urlencode({"q": city, "appid": api_key, "units": units})
        with urlopen(f"https://api.openweathermap.org/data/2.5/weather?{qs}", timeout=5) as resp:
            payload = resp.read().decode("utf-8", errors="replace")

        # Avoid adding new dependencies; parse minimal JSON ourselves
        import json

        data = json.loads(payload)
        main = data.get("main") or {}
        temp = main.get("temp")
        humidity = main.get("humidity")

        if temp is None or humidity is None:
            return None

        return {"temperature": float(temp), "humidity": int(humidity), "source": "openweather", "city": city}
    except Exception:
        return None

def generate_prediction():

    while True:

        now = datetime.now()

        weather = _fetch_weather()
        if weather:
            temperature = weather["temperature"]
            humidity = weather["humidity"]
            weather_source = weather["source"]
            weather_city = weather["city"]
        else:
            temperature = random.randint(28, 36)
            humidity = random.randint(50, 70)
            weather_source = "random"
            weather_city = None

        weekday = now.isoweekday()  # 1=Mon ... 7=Sun
        hour = now.hour

        input_data = pd.DataFrame(
            [[temperature, humidity, weekday, hour]],
            columns=["temperature", "humidity", "weekday", "hour"],
        )

        prediction = model.predict(input_data)

        data = {
            "temperature": temperature,
            "humidity": humidity,
            "weekday": weekday,
            "hour": hour,
            "predicted_load": int(prediction[0])
        }

        if weather_city:
            data["weather_city"] = weather_city
        data["weather_source"] = weather_source

        print("Sending:",data)

        socketio.emit("load_update",data)

        time.sleep(3)


@app.route("/")
def home():
    return "Cafeteria Prediction Server Running"


if __name__ == "__main__":

    thread = threading.Thread(target=generate_prediction)
    thread.start()

    socketio.run(app,port=5000)