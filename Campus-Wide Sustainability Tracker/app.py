import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import plotly.express as px

st.set_page_config(page_title="Campus Sustainability Tracker", layout="wide")

st.title("Campus-Wide Sustainability Tracker")

# -----------------------
# Create Sample Dataset
# -----------------------
data = {
    "day":[1,2,3,4,5,6,7,8,9,10],
    "electricity_kwh":[1200,1150,1300,1280,1350,1400,1380,1420,1450,1480],
    "water_liters":[9000,8700,9100,8800,9200,9400,9300,9500,9600,9700],
    "waste_kg":[300,290,320,310,305,330,325,340,350,360],
    "renewable_kwh":[150,170,200,220,240,260,280,300,320,340]
}

df = pd.DataFrame(data)

# -----------------------
# Carbon Calculations
# -----------------------
EMISSION_FACTOR = 0.82

df["carbon_emission"] = df["electricity_kwh"] * EMISSION_FACTOR
df["carbon_saved"] = df["renewable_kwh"] * EMISSION_FACTOR

# -----------------------
# Machine Learning Model
# -----------------------
X = df[["day"]]
y = df["electricity_kwh"]

model = LinearRegression()
model.fit(X, y)

next_day = np.array([[df["day"].max()+1]])
prediction = model.predict(next_day)[0]

# -----------------------
# KPI Metrics
# -----------------------
total_energy = int(df["electricity_kwh"].sum())
total_water = int(df["water_liters"].sum())
total_waste = int(df["waste_kg"].sum())
total_carbon = int(df["carbon_emission"].sum())

c1,c2,c3,c4 = st.columns(4)

c1.metric("Total Electricity", f"{total_energy} kWh")
c2.metric("Total Water", f"{total_water} L")
c3.metric("Total Waste", f"{total_waste} kg")
c4.metric("Carbon Emission", f"{total_carbon} kg CO2")

st.metric("Predicted Electricity Next Day", f"{int(prediction)} kWh")

st.divider()

# -----------------------
# Charts
# -----------------------
st.subheader("Electricity Consumption Trend")
fig1 = px.line(df,x="day",y="electricity_kwh")
st.plotly_chart(fig1,use_container_width=True)

st.subheader("Renewable Energy Production")
fig2 = px.line(df,x="day",y="renewable_kwh")
st.plotly_chart(fig2,use_container_width=True)

st.subheader("Water Usage")
fig3 = px.bar(df,x="day",y="water_liters")
st.plotly_chart(fig3,use_container_width=True)

st.subheader("Waste Generation")
fig4 = px.bar(df,x="day",y="waste_kg")
st.plotly_chart(fig4,use_container_width=True)

st.divider()

# -----------------------
# Drill Down
# -----------------------
st.subheader("Drill Down Analysis")

metric = st.selectbox(
"Select Metric",
["electricity_kwh","water_liters","waste_kg","renewable_kwh"]
)

fig5 = px.line(df,x="day",y=metric,title=f"{metric} Trend")
st.plotly_chart(fig5,use_container_width=True)

# -----------------------
# Raw Data
# -----------------------
st.subheader("Dataset")
st.dataframe(df)