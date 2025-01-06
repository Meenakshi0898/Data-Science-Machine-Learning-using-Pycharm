import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

# Example Time Series Data
data = [12, 15, 14, 17, 19, 21, 25, 23, 22, 24, 28]
df = pd.Series(data)

# Fit ARIMA Model
model = ARIMA(df, order=(1, 1, 1))  # ARIMA(p=1, d=1, q=1)
model_fit = model.fit()

# Forecast Next 3 Values    
forecast = model_fit.forecast(steps=3)
print("Forecasted Values:", forecast)

# Plot Original Data and Forecast
plt.plot(df, label="Original Data")
plt.plot(range(len(df), len(df) + 3), forecast, label="Forecast", color="red")
plt.legend()
plt.show()
