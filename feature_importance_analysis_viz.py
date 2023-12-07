import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV data file
data = pd.read_csv('./data/data.csv')

# Transform 'tag' into a binary target variable (1 for clicks, 0 for non-clicks)
data['click'] = data['tag'].apply(lambda x: 1 if 'fclick' in x else 0)

# Exclude the 'Unnamed: 0', 'tag', and 'uid' columns from the analysis
data = data.drop(columns=['Unnamed: 0', 'tag', 'uid'])

# Transform any categorical columns
label_encoders = {}
for column in data.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    data[column] = le.fit_transform(data[column])
    label_encoders[column] = le

# Split the dataset into features and target
y = data['click']
X = data.drop(columns=['click'])

# Train a Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Get feature importance
importances = model.feature_importances_
indices = np.argsort(importances)

# Plot feature importance
plt.title('Feature Importances')
plt.barh(range(len(indices)), importances[indices], color='b', align='center')
plt.yticks(range(len(indices)), [X.columns[i] for i in indices])
plt.xlabel('Relative Importance')
plt.savefig('feature_importance.png')
plt.show()
