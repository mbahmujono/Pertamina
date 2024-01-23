import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller
import warnings

warnings.filterwarnings("ignore")  # Ignore convergence warnings

# Function to check stationarity
def check_stationarity(series):
    result = adfuller(series)
    p_value = result[1]
    return p_value <= 0.05  # Data is stationary if p-value is less than 0.05

# ARIMA forecasting function
def forecast_with_arima(data, column, order, steps=5):
    """
    Forecast using ARIMA model.

    :param data: Pandas DataFrame containing the time series data.
    :param column: Column name of the time series in the DataFrame.
    :param order: The (p, d, q) order of the ARIMA model.
    :param steps: Number of future steps to forecast.
    :return: Forecasted value.
    """
    # Ensure data is stationary
    if not check_stationarity(data[column]):
        raise ValueError("Time series data is not stationary. Please differenciate or transform the data.")

    # Fit the ARIMA model
    model = ARIMA(data[column], order=order)
    model_fit = model.fit()
    print(model_fit.summary())

    forecast = model_fit.forecast(steps=steps)
    print(forecast)

    return forecast
# Example usage
# Assuming 'df' is your DataFrame and 'sales' is the column you want to forecast
# Example: forecast_with
