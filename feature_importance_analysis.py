import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Read the CSV data file
data = pd.read_csv('./data/data.csv')

# Transform 'tag' into a binary target variable (1 for clicks, 0 for non-clicks)
data['click'] = data['tag'].apply(lambda x: 1 if 'fclick' in x else 0)

# Exclude the 'tag' and 'uid' columns from the analysis
data = data.drop(columns=['tag', 'uid'])

# Transform any categorical columns
label_encoders = {}
for column in data.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    data[column] = le.fit_transform(data[column])
    label_encoders[column] = le

# Split the dataset into features and the target (clicks)
y = data['click']
X = data.drop(columns=['click'])

# Train a Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Get feature importance
feature_importances = model.feature_importances_

# Create a DataFrame and sort by importance
features = pd.DataFrame(
    {
        'feature': X.columns,
        'importance': feature_importances
    }
).sort_values(by='importance', ascending=False)

# Print the ranked list of features by importance
print(features.to_dict('records'))