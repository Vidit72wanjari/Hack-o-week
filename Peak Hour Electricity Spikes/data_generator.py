import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_data(days=365):
    start = datetime.now() - timedelta(days=days)
    hours = days * 24

    timestamps = [start + timedelta(hours=i) for i in range(hours)]
    data = []

    for ts in timestamps:
        hour = ts.hour
        day_of_year = ts.timetuple().tm_yday

        base = 30

        # Daily cycle
        daily_cycle = 10 * np.sin((hour / 24) * 2 * np.pi)

        # Realistic evening Gaussian peak (around 8PM)
        evening_peak = 35 * np.exp(-0.5 * ((hour - 20) / 2)**2)

        # Seasonal yearly pattern
        seasonal = 15 * np.sin((day_of_year / 365) * 2 * np.pi)

        noise = np.random.normal(0, 4)

        kwh = base + daily_cycle + evening_peak + seasonal + noise
        data.append([ts, max(kwh, 5)])

    df = pd.DataFrame(data, columns=["timestamp", "kwh"])
    return df