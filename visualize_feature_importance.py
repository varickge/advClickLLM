import pandas as pd
import matplotlib.pyplot as plt
import joblib
import numpy as np

# Load the data
data = pd.read_csv('./data/data.csv')

# Preprocessing - exclude 'tag', convert categorical
X = data.drop(['tag'], axis=1)
for column in X.select_dtypes(include=['object']).columns:
    X[column] = X[column].astype('category').cat.codes

# Load the trained Logistic Regression model
model = joblib.load('ad_click_model.sav')

# Get coefficients from the model and take the absolute value
coefficients = np.abs(model.coef_[0])

# Match coefficients to features
feature_names = X.columns

# Create a DataFrame for plotting
feature_importance_df = pd.DataFrame({'feature': feature_names, 'importance': coefficients})

# Sort the DataFrame by importance
feature_importance_ordered = feature_importance_df.sort_values('importance')

# Plotting
plt.figure(figsize=(10, 8))
plt.barh(feature_importance_ordered['feature'], feature_importance_ordered['importance'], color='skyblue')
plt.xlabel('Feature Importance')
plt.title('Feature Importance for Ad Click Prediction')
plt.tight_layout()
plt.savefig('feature_importance.png')
plt.show()
