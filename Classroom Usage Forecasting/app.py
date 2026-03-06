import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

from data_generator import generate_data
from model import forecast_future

app = dash.Dash(__name__)

df_full = generate_data(7)

app.layout = html.Div([
    html.H2("Classroom Usage Forecast (ARIMA)"),
    dcc.Graph(id="graph")
])

@app.callback(
    Output("graph", "figure"),
    Input("graph", "id")
)
def update_dashboard(_):

    df = df_full.copy()

    forecast, conf_int = forecast_future(df, steps=6)

    last_time = df["timestamp"].iloc[-1]
    future_times = [last_time + pd.Timedelta(hours=i+1) for i in range(6)]

    fig = go.Figure()

    # Historical electricity
    fig.add_trace(go.Scatter(
        x=df["timestamp"],
        y=df["electricity"],
        mode="lines",
        name="Historical Usage"
    ))

    # Forecast line
    fig.add_trace(go.Scatter(
        x=future_times,
        y=forecast,
        mode="lines+markers",
        name="Forecast"
    ))

    # Confidence interval shading
    fig.add_trace(go.Scatter(
        x=future_times + future_times[::-1],
        y=list(conf_int.iloc[:,0]) + list(conf_int.iloc[:,1])[::-1],
        fill="toself",
        fillcolor="rgba(255,0,0,0.2)",
        line=dict(color="rgba(255,0,0,0)"),
        hoverinfo="skip",
        showlegend=True,
        name="95% Confidence Interval"
    ))

    fig.update_layout(
        xaxis=dict(tickformat="%d %b %Y %I:%M %p"),
        yaxis_title="Electricity (kWh)"
    )

    return fig
if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=8060,
        debug=False
    )