import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression

# Load data
data = pd.read_csv('./data/data.csv')

# Preprocess data
def preprocess_data(data):
    X = data.drop(['tag'], axis=1)
    y = data['tag'].apply(lambda x: 1 if 'click' in x else 0)
    label_encoders = {}
    for column in X.select_dtypes(include=['object']).columns:
        le = LabelEncoder()
        X[column] = le.fit_transform(X[column])
        label_encoders[column] = le
    return X, y, label_encoders

X, y, label_encoders = preprocess_data(data)

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize Logistic Regression model
logreg = LogisticRegression(max_iter=1000)

# Train model
logreg.fit(X_train, y_train)

# Function to predict probabilities for new data points
def predict_probabilities(new_data, label_encoders):
    for column in new_data.select_dtypes(include=['object']).columns:
        le = label_encoders[column]
        new_data[column] = le.transform(new_data[column])
    return logreg.predict_proba(new_data)[:, 1]

# Save the model and label encoders along with preprocessing function
def save_model():
    import joblib
    model_filename = 'ad_click_model.sav'
    le_filename = 'label_encoders.sav'
    joblib.dump(logreg, model_filename)
    joblib.dump(label_encoders, le_filename)
    print(f'Model and label encoders saved to {model_filename} and {le_filename}, respectively.')

save_model()
