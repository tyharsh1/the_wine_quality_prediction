import streamlit as st
import pandas as pd

def drinks_page():
    st.title("All Drinks")
    st.write("This page shows information about wines and beers.")

    # Load your CSV or sample data
    try:
        df = pd.read_csv("data/winequality.csv")
        st.subheader("Wine Dataset")
        st.dataframe(df)
    except FileNotFoundError:
        st.error("winequality.csv not found in /data folder.")
