import pickle
import numpy as np

# Good wine input (as per your image)
input_data = {
    'fixed acidity': 13.0,
    'volatile acidity': 1.2,
    'citric acid': 0.0,
    'residual sugar': 15.0,
    'chlorides': 0.1,
    'free sulfur dioxide': 5.0,
    'total sulfur dioxide': 300.0,
    'density': 1.010,
    'pH': 2.8,
    'sulphates': 0.2,
    'alcohol': 8.0
}

# Feature order (must match training order)
feature_order = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
                 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
                 'pH', 'sulphates', 'alcohol']

# Convert to numpy array
input_values = np.array([input_data[feature] for feature in feature_order]).reshape(1, -1)

# Load scaler and model
with open('models/scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

with open('models/model.pkl', 'rb') as f:
    model = pickle.load(f)

# Scale input
scaled_input = scaler.transform(input_values)

# Predict
prediction = model.predict(scaled_input)[0]
print(f"Predicted Quality Score: {prediction:.2f}")

# Categorize
if prediction >= 7:
    category = "Good Quality"
elif prediction >= 5:
    category = "Average Quality"
else:
    category = "Bad Quality"

print(f"Predicted Category: {category}")