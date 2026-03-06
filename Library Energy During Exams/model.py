from statsmodels.tsa.holtwinters import ExponentialSmoothing

def forecast_semester_end(df, steps=7):

    series = df["energy"]

    model = ExponentialSmoothing(
        series,
        trend="add",
        seasonal="add",
        seasonal_periods=7
    )

    fit = model.fit()

    forecast = fit.forecast(steps)

    return {
        "forecast_mean": forecast.mean(),
        "forecast_series": forecast
    }