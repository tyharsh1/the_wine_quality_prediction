from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

print("Starting app...")

# Load model and scaler
print("Loading model and scaler...")
with open('models/model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('models/scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

print("Model and scaler loaded successfully.")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(request.form[f]) for f in [
            'fixed_acidity', 'volatile_acidity', 'citric_acid', 'residual_sugar',
            'chlorides', 'free_sulfur_dioxide', 'total_sulfur_dioxide',
            'density', 'pH', 'sulphates', 'alcohol'
        ]]
        input_array = np.array([features])
        input_scaled = scaler.transform(input_array)
        prediction = model.predict(input_scaled)[0]

        # Categorize the prediction
        if prediction >= 7.5:
            quality_text = "Good Quality"
        elif prediction >= 5.5:
            quality_text = "Average Quality"
        else:
            quality_text = "Poor Quality"

        return render_template('result.html', prediction=round(prediction, 2), quality_text=quality_text)

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)