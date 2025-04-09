import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Wine Quality Prediction", layout="centered")

def main():
    selected = option_menu(
        menu_title=None,
        options=["Home", "Predict", "Model Info", "Data Visualization", "All Drinks"],
        icons=["house", "bar-chart", "info", "graph-up", "cup-straw"],
        orientation="horizontal",
    )

    if selected == "Home":
        st.title("Welcome to the Wine Quality Predictor!")
        st.write("Use the menu to navigate.")
    elif selected == "Predict":
        from Predict import predict_page
        predict_page()
    elif selected == "Model Info":
        from Model_Info import model_info
        model_info()
    elif selected == "Data Visualization":
        from Data_Visualization import show_visuals
        show_visuals()
    elif selected == "All Drinks":
        from All_Drinks import drinks_page
        drinks_page()

if __name__ == "__main__":
    main()
