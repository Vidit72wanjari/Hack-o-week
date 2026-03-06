import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

from data_generator import generate_data
from model import preprocess, train_model, predict_peak

app = dash.Dash(__name__)

# Generate ONCE
df_full = preprocess(generate_data(365))

app.layout = html.Div([
    html.H2("Dorm Electricity Usage Dashboard"),

    dcc.Dropdown(
        id="view-mode",
        options=[
            {"label": "Daily", "value": "D"},
            {"label": "Monthly", "value": "M"},
            {"label": "Yearly", "value": "Y"}
        ],
        value="D",
        style={"width": "200px"}
    ),

    dcc.Graph(id="graph"),

    html.Div(id="peak-output", style={"marginTop": "20px"}),

    dcc.Interval(
        id="interval",
        interval=60*1000,
        n_intervals=0
    )
])


@app.callback(
    [Output("graph", "figure"),
     Output("peak-output", "children")],
    [Input("interval", "n_intervals"),
     Input("view-mode", "value")]
)
def update_dashboard(n, view_mode):
    global df_full

    df = df_full.copy()

    model = train_model(df)
    peak_hour = predict_peak(model, df)

    if view_mode == "D":
        df_view = df.tail(24)
    elif view_mode == "M":
        df_view = df.tail(24 * 30)
    else:
        df_view = df

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df_view["timestamp"],
        y=df_view["kwh"],
        mode="lines",
        name="Actual Usage"
    ))

    fig.add_trace(go.Scatter(
        x=df_view["timestamp"],
        y=df_view["smoothed"],
        mode="lines",
        name="Smoothed"
    ))

    fig.update_layout(
        xaxis=dict(
            tickformat="%d %b %I:%M %p"
        ),
        yaxis_title="Electricity (kWh)"
    )

    peak_time_12hr = pd.to_datetime(f"{peak_hour}:00").strftime("%I:%M %p")

    return fig, f"Predicted Tomorrow Peak: {peak_time_12hr}"


if __name__ == "__main__":
    app.run(debug=True)