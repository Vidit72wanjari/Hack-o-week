import pandas as pd

def generate_event_calendar(days=180):

    start = pd.Timestamp.today() - pd.Timedelta(days=days)

    dates = pd.date_range(start=start, periods=days)

    exam_flag = []

    for i in range(len(dates)):

        # simulate exam weeks
        if 60 <= i <= 80 or 140 <= i <= 160:
            exam_flag.append(1)
        else:
            exam_flag.append(0)

    event_df = pd.DataFrame({
        "date": dates,
        "exam_flag": exam_flag
    })

    return event_df