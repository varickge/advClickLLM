import pandas as pd

# Load data
data = pd.read_csv('./data/data.csv')

# Filter out clicks
click_data = data[data['tag'].str.contains('click')]

# Count the number of clicks for each type of device
device_clicks = click_data['hardware'].value_counts().reset_index()
device_clicks.columns = ['hardware', 'clicks']

# Display ordered list of device types by number of clicks
print(device_clicks)
