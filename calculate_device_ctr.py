import pandas as pd

# Load data
data = pd.read_csv('./data/data.csv')

# Calculate clicks and impressions for each device
results = data.groupby('hardware')['tag'].agg(['count', lambda x: x.str.contains('click').sum()]).rename(columns={'count': 'impressions', '<lambda_0>': 'clicks'})

# Calculate CTR for each device
results['CTR'] = results['clicks'] / results['impressions']

# Sort devices by CTR in descending order
ordered_results = results.sort_values('CTR', ascending=False).reset_index()

# Display ordered list of (device, CTR)
print(ordered_results[['hardware', 'CTR']])
