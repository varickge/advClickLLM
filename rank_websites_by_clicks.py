import pandas as pd

# Load data
data = pd.read_csv('./data/data.csv')

# Filter out clicks
clicks_data = data[data['tag'].str.contains('click')]

# Count the number of clicks for each website (site_id)
site_clicks = clicks_data['site_id'].value_counts().head(15).reset_index()
site_clicks.columns = ['site_id', 'clicks']

# Display ordered list of top 15 websites by number of clicks
print(site_clicks)
