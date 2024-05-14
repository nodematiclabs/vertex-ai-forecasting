import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set the starting date and number of days
start_date = datetime.now()
num_days = 2500

# Generate a date range
dates = [start_date + timedelta(days=i) for i in range(num_days)]

# Generate sales data with a trend
sales = [100 + i * 10 + np.random.normal(0, 10) for i in range(num_days)]  # Base sales, increment, and some noise

# Create a DataFrame
data = pd.DataFrame({
    'date': dates,
    'sales': sales,
    'series': "sales"
})

# Convert the date column to the TIMESTAMP format for BigQuery
data['date'] = pd.to_datetime(data['date']).dt.strftime('%Y-%m-%d %H:%M:%S')

# Save to CSV
data.to_csv('sales_data.csv', index=False)

print(data)
