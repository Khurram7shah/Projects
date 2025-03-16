

import streamlit as st
import pandas as pd

# Title
st.title("BMI Calculator 🏋️")

# User inputs
height = st.slider("Enter your height (in cm)", 100, 250, 175)
weight = st.slider("Enter your weight (in kg)", 40, 200, 70)

# BMI Calculation
bmi = weight / ((height / 100) ** 2)

# Display BMI Result
st.write(f"## Your BMI is **{bmi:.2f}**")

# Determine BMI Category
if bmi < 18.5:   
    category = "Underweight 😕"
elif 18.5 <= bmi < 25:
    category = "Normal weight 😊"
elif 25 <= bmi < 30:
    category = "Overweight 😐"
else:
    category = "Obesity 😞"

st.write(f"### Category: {category}")

# BMI Categories
st.write("### 📌 BMI Categories:")
st.write("- **Underweight** : BMI less than **18.5**")
st.write("- **Normal weight** : BMI between **18.5 and 24.9**")
st.write("- **Overweight** : BMI between **25 and 29.9**")
st.write("- **Obesity** : BMI **30 or greater**")
