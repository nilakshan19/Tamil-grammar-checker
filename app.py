# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LQ2S9hH456vt9Daq2GHm-qy-Z7xszypV
"""

import streamlit as st
import joblib
import numpy as np

# Load the trained model and vectorizer
model = joblib.load("ml_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

def predict_sentence(sentence):
    """Predict whether the given sentence is grammatically correct."""
    vectorized_input = vectorizer.transform([sentence])
    prediction = model.predict(vectorized_input)
    return "Correct" if prediction[0] == 1 else "Error"

# Streamlit app
st.title("Tamil Grammar Checker")

st.write("""
**Assignment 2:** Tamil Grammar Checker
- **Objective:** Build a grammar checker for Tamil sentences using machine learning models.
- **Team Members:**
  - 2020E026
  - 2020E106
Enter a Tamil sentence below, and the app will predict whether it is grammatically correct or not.
""")

# Input form
user_input = st.text_area("Enter a Tamil sentence:", height=100)

if st.button("Check Grammar"):
    if user_input.strip():
        prediction = predict_sentence(user_input)
        st.success(f"Prediction: {prediction}")
    else:
        st.error("Please enter a valid sentence.")

# Add Assignment details
st.write("---")
st.write("### Assignment Details")
st.write("""


**This application uses a machine learning model trained on Tamil sentences. The model predicts whether a given sentence is grammatically correct or contains errors.**
""")

st.write("---")
st.write("This application uses a Machine Learning model trained on Tamil sentences.")
