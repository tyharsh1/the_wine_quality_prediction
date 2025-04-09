import os
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def show_visuals():
    st.title("Wine Quality Data Visualizations")

    # Dynamically get correct path
    base_dir = os.path.dirname(os.path.dirname(__file__))  # go up one level from streamlit_app/
    data_path = os.path.join(base_dir, "data", "winequality.csv")

    data = pd.read_csv(data_path)

    st.write("### Correlation Heatmap")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(data.corr(), annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

    st.write("### Alcohol vs Quality")
    fig2, ax2 = plt.subplots()
    sns.boxplot(x="quality", y="alcohol", data=data, ax=ax2)
    st.pyplot(fig2)
