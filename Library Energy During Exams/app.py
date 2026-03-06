import streamlit as st
import pandas as pd

from data_generator import generate_data
from model import forecast_semester_end

st.set_page_config(page_title="Library Energy Forecast", layout="wide")

st.title("Library Energy Consumption During Exams")

df = generate_data(180)

if len(df) == 0:
    st.error("Dataset empty")
    st.stop()

result = forecast_semester_end(df, steps=7)

forecast_series = result["forecast_series"]
forecast_value = result["forecast_mean"]

col1, col2 = st.columns(2)

with col1:
    st.subheader("Historical Energy Usage")
    st.line_chart(df.set_index("date")["energy"])

with col2:
    st.subheader("Forecast Next 7 Days")

    future_dates = pd.date_range(
        start=df["date"].iloc[-1] + pd.Timedelta(days=1),
        periods=7
    )

    forecast_df = pd.DataFrame({
        "date": future_dates,
        "forecast_energy": forecast_series.values
    })

    st.line_chart(forecast_df.set_index("date"))

st.metric(
    label="Predicted Average Energy Usage (Next 7 Days)",
    value=round(forecast_value, 2)
)