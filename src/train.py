from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

def train_model(X_train, y_train, X_test, y_test, model_path='models/model.pkl'):
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Prediction and accuracy
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print(f"Model Accuracy: {accuracy:.2f}")

    # Save the model
    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")

    return model