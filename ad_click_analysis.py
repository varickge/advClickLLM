import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Load data
data = pd.read_csv('./data/data.csv')

# Preprocess data
X = data.drop(['tag'], axis=1)
y = data['tag'].apply(lambda x: 1 if 'click' in x else 0)

# Convert categorical variables to numerical values
label_encoders = {}
for column in X.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    X[column] = le.fit_transform(X[column])
    label_encoders[column] = le

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize Random Forest classifier
rf_clf = RandomForestClassifier(n_estimators=100, random_state=42)

# Train classifier
rf_clf.fit(X_train, y_train)

# Get feature importances
feature_importances = rf_clf.feature_importances_

# Map feature importances to the feature names
importance_dict = dict(zip(X.columns, feature_importances))

# Print importance
for feature in sorted(importance_dict, key=importance_dict.get, reverse=True):
    print(f'{feature}: {importance_dict[feature]}\n')
