import streamlit as st
import pandas as pd
import numpy as np

# --- Display Elements (slide 03) ---
st.title("Sales Dashboard")
st.markdown("Revenue is **up 12%** this quarter.")
st.write({"users": 1280, "growth": 0.12})

df = pd.DataFrame({
    "month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "revenue": [12000, 15000, 13500, 18000, 21000],
})
st.dataframe(df)
st.metric("Revenue", "$48.2k", "+12%")
st.line_chart(df.set_index("month"))

# --- Input Widgets (slide 04) ---
name = st.text_input("Name")
age = st.slider("Age", 0, 100, 25)
agree = st.checkbox("I accept the terms")
flavor = st.selectbox("Pick one", ["Vanilla", "Mango", "Mint"])

if st.button("Submit"):
    st.write(f"{name} is {age} and likes {flavor}.")