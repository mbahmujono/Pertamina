import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

# Sample data loading (replace this with your actual data loading code)
data = {
    'City': ['City_E'] * 5,
    'timestamp': ['2024-01-19 04:31:00', '2024-01-19 04:32:00', '2024-01-19 04:33:00', 
                 '2024-01-19 10:16:00', '2024-01-19 10:17:00'],
    'sales': ["4,383.8159", "12,048.8855", "8,888.7808", "7,615.162", "14,224.0271"]
}
df = pd.DataFrame(data)

# Convert timestamp to datetime and set as index
df['timestamp'] = pd.to_datetime(df['timestamp'])
df.set_index('timestamp', inplace=True)

# Convert sales to numerical values
df['sales'] = df['sales'].str.replace(',', '').astype(float)

# Resample and fill missing data (assuming constant value filling)
df_resampled = df.resample('T').sum().fillna(0)

# ARIMA Model - Example with (1, 1, 0)
model = ARIMA(df_resampled['sales'], order=(1, 1, 0))
model_fit = model.fit()

# Forecasting
forecast = model_fit.forecast(steps=5)
print(forecast)