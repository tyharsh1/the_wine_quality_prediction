import streamlit as st

def model_info():
    st.title("Model Information")

    st.write("""
    This app uses a Gradient Boosting Regressor model to predict wine quality based on physicochemical inputs.
    The model was trained on a dataset with features like acidity, residual sugar, sulphates, etc.
    """)

    if "prediction_value" in st.session_state:
        st.subheader("Last Predicted Result")
        st.write(f"**Predicted Quality Score:** {st.session_state.prediction_value}")
        st.write(f"**Category:** {st.session_state.prediction_category}")
    else:
        st.info("No prediction has been made yet. Please make a prediction to see results here.")
