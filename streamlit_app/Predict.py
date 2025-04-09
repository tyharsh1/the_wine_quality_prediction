import streamlit as st
import numpy as np
import pickle
import os

def predict_page():
    st.title("Wine Quality Prediction")

    # Load model and scaler
    try:
        with open("models/model.pkl", "rb") as f:
            model = pickle.load(f)
        with open("models/scaler.pkl", "rb") as f:
            scaler = pickle.load(f)
    except FileNotFoundError:
        st.error("Model or scaler file not found. Please train the model first.")
        return
    except pickle.UnpicklingError:
        st.error("Error loading model or scaler. The file might be corrupted.")
        return

    st.subheader("Enter wine physicochemical properties:")

    # Set default average values for inputs based on typical wine data
    default_values = {
        "fixed_acidity": 7.0,
        "volatile_acidity": 0.5,
        "citric_acid": 0.3,
        "residual_sugar": 2.5,
        "chlorides": 0.05,
        "free_sulfur_dioxide": 15.0,
        "total_sulfur_dioxide": 50.0,
        "density": 0.994,
        "pH": 3.3,
        "sulphates": 0.5,
        "alcohol": 10.0,
    }

    # Initialize session state if not already present
    for key, val in default_values.items():
        if key not in st.session_state:
            st.session_state[key] = val

    # Input fields with session state values
    st.session_state.fixed_acidity = st.number_input("Fixed Acidity", step=0.1, value=st.session_state.fixed_acidity)
    st.session_state.volatile_acidity = st.number_input("Volatile Acidity", step=0.01, value=st.session_state.volatile_acidity)
    st.session_state.citric_acid = st.number_input("Citric Acid", step=0.01, value=st.session_state.citric_acid)
    st.session_state.residual_sugar = st.number_input("Residual Sugar", step=0.1, value=st.session_state.residual_sugar)
    st.session_state.chlorides = st.number_input("Chlorides", step=0.001, value=st.session_state.chlorides)
    st.session_state.free_sulfur_dioxide = st.number_input("Free Sulfur Dioxide", step=0.1, value=st.session_state.free_sulfur_dioxide)
    st.session_state.total_sulfur_dioxide = st.number_input("Total Sulfur Dioxide", step=0.1, value=st.session_state.total_sulfur_dioxide)
    st.session_state.density = st.number_input("Density", step=0.0001, format="%.5f", value=st.session_state.density)
    st.session_state.pH = st.number_input("pH", step=0.01, value=st.session_state.pH)
    st.session_state.sulphates = st.number_input("Sulphates", step=0.01, value=st.session_state.sulphates)
    st.session_state.alcohol = st.number_input("Alcohol", step=0.1, value=st.session_state.alcohol)

    if st.button("Predict Quality"):
        inputs = [
            st.session_state.fixed_acidity,
            st.session_state.volatile_acidity,
            st.session_state.citric_acid,
            st.session_state.residual_sugar,
            st.session_state.chlorides,
            st.session_state.free_sulfur_dioxide,
            st.session_state.total_sulfur_dioxide,
            st.session_state.density,
            st.session_state.pH,
            st.session_state.sulphates,
            st.session_state.alcohol,
        ]

        if any(val is None for val in inputs):
            st.warning("Please fill in all values before predicting.")
            return

        input_array = np.array([inputs])
        scaled_input = scaler.transform(input_array)
        prediction = model.predict(scaled_input)[0]
        prediction_rounded = round(prediction)

        # Display prediction
        st.success(f"Predicted Wine Quality: {prediction_rounded}")

        # Quality category
        if prediction_rounded <= 4:
            quality = "Bad"
        elif prediction_rounded <= 6:
            quality = "Average"
        else:
            quality = "Good"

        st.info(f"Wine Quality Category: **{quality}**")

        # Save values in session state for use in Model Info page
        st.session_state.prediction_value = prediction_rounded
        st.session_state.prediction_category = quality