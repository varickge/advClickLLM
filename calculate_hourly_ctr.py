import pandas as pd
from datetime import datetime

# Load data
data = pd.read_csv('./data/data.csv')

# Convert 'reg_time' to datetime and extract hour
data['hour'] = pd.to_datetime(data['reg_time']).dt.hour

# Calculate clicks and impressions for each hour
hourly_results = data.groupby('hour')['tag'].agg(['count', lambda x: (x.str.contains('click')).sum()]).rename(columns={'count': 'impressions', '<lambda_0>': 'clicks'})

# Calculate CTR for each hour
hourly_results['CTR'] = hourly_results['clicks'] / hourly_results['impressions']

# Sort hours by CTR in descending order
ordered_hourly_results = hourly_results.sort_values('CTR', ascending=False).reset_index()

# Display top 5 hours in ordered list of (hour, CTR)
top_5_hours = ordered_hourly_results.head(5)
print(top_5_hours[['hour', 'CTR']])
