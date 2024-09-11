# Needed Modules
import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error

# Read CSV file
df = pd.read_csv('Time-Series-Prediction\daily_temperature.csv')

# Convert Dates to Date Times and sort them
df['Date'] = pd.to_datetime(df['Date'])
df.sort_values('Date', inplace=True)

# Prepare the dataset for Prophet
df_prophet = df.rename(columns={'Date': 'ds', 'Temperature': 'y'})

# Selecting New York City
ds_prophet = df.rename(df_prophet['City'] == 'New York')

# Initialize and fit the model
model = Prophet(daily_seasonality=True)
model.fit(df_prophet)

# Making a dataframe for predictions
future = model.make_future_dataframe(periods=0)
forecast = model.predict(future)

# Merge the data
df_prophet.set_index('ds', inplace=True)
forecast.set_index('ds', inplace=True)
df_merged = df_prophet.join(forecast[['yhat', 'yhat_lower', 'yhat_upper']], how='inner')

# Reset Index
df_merged.reset_index(inplace=True)

# Mean Absolute Error
y_test = df_merged['y'].values
prediction = df_merged['yhat'].values

mae = mean_absolute_error(y_test, prediction)
print(f'Mean Absolute Error: {mae}')

# Plot the actual vs predicted temperatures
plt.figure(figsize=(10, 6))
plt.plot(df_merged['ds'], df_merged['y'], 'b-', label='Actual Temperature', marker="o", markersize=8)
plt.plot(df_merged['ds'], df_merged['yhat'], '-r', label='Predicted Temperature', marker='o', markersize=8)

for i, txt in enumerate(df_merged['y']):
    plt.annotate(round(txt, 2), (df_merged['ds'][i], df_merged['y'][i]), textcoords='offset points', xytext=(0, 10), ha='center')

for i, txt in enumerate(df_merged['yhat']):
    plt.annotate(round(txt, 2), (df_merged['ds'][i], df_merged['yhat'][i]), textcoords='offset points', xytext=(0, 10), ha='center')


# Run functions
plt.legend()
plt.xlabel('Date')
plt.ylabel('Temperature')
plt.title('Actual vs Predicted Temperatures')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()