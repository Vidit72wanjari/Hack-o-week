from statsmodels.tsa.arima.model import ARIMA

def forecast_future(df, steps=6):
    series = df["electricity"]

    model = ARIMA(series, order=(2,1,2))
    model_fit = model.fit()

    forecast_obj = model_fit.get_forecast(steps=steps)

    forecast = forecast_obj.predicted_mean
    conf_int = forecast_obj.conf_int(alpha=0.05)

    return forecast, conf_int