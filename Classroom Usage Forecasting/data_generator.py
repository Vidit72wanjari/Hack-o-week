import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_data(days=7):
    end = datetime.now()
    start = end - timedelta(days=days)

    timestamps = pd.date_range(start=start, end=end, freq="H")

    data = []

    for ts in timestamps:
        hour = ts.hour
        weekday = ts.weekday()

        # Base occupancy
        occupancy = 5

        if weekday < 5:  # Weekdays only

            # Morning build-up
            morning = 20 * np.exp(-0.5 * ((hour - 10) / 2)**2)

            # Lunch drop at 1 PM
            lunch_drop = -15 * np.exp(-0.5 * ((hour - 13) / 1.2)**2)

            # Afternoon peak centered at 3 PM
            afternoon_peak = 35 * np.exp(-0.5 * ((hour - 15) / 1.5)**2)

            occupancy = 10 + morning + lunch_drop + afternoon_peak

        occupancy += np.random.normal(0, 2)
        occupancy = max(0, occupancy)

        # Electricity proportional to occupancy
        electricity = 15 + 1.0 * occupancy + np.random.normal(0, 2)

        data.append([ts, occupancy, electricity])

    df = pd.DataFrame(data, columns=["timestamp", "occupancy", "electricity"])
    return df