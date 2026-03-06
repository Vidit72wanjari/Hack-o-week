import pandas as pd
import numpy as np
from event_calendar import generate_event_calendar

def generate_data(days=180):

    start = pd.Timestamp.today() - pd.Timedelta(days=days)
    dates = pd.date_range(start=start, periods=days)

    event_df = generate_event_calendar(days)

    data = []

    for i, date in enumerate(dates):

        weekday = date.weekday()

        base = 50

        # weekday pattern
        if weekday < 5:
            base += 15
        else:
            base -= 10

        # gradual trend
        trend = i * 0.05

        noise = np.random.normal(0,5)

        data.append([date, base + trend + noise])

    df_energy = pd.DataFrame(data, columns=["date","base_energy"])

    df = df_energy.merge(event_df, on="date", how="left")
    df["exam_flag"] = df["exam_flag"].fillna(0)

    df["energy"] = (
        df["base_energy"]
        + df["exam_flag"] * 60
    )

    return df[["date","energy","exam_flag"]]