import pytest
import pickle
import numpy as np

def test_model_prediction():
    model = pickle.load(open("models/model.pkl", "rb"))
    sample = np.array([[7.4, 0.7, 0.0, 1.9, 0.076, 11.0, 34.0, 0.9978, 3.51, 0.56, 9.4]])
    prediction = model.predict(sample)
    assert prediction[0] in range(0, 11)
