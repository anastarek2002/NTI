import streamlit as st
import pandas as pd
import numpy as np

# --- Layout (slide 05) ---
with st.sidebar:
    theme = st.radio("Theme", ["Light", "Dark"])
    steps = st.slider("Steps", 10, 500, 100)
    seed = st.number_input("Seed", value=42)

c1, c2, c3 = st.columns(3)

# --- State & Caching (slide 06) ---
@st.cache_data
def load_data(path):
    return pd.read_csv(path) if False else None

if "count" not in st.session_state:
    st.session_state.count = 0
if st.button("+1"):
    st.session_state.count += 1

# --- Full Example (slide 07) ---
st.title("Random Walk Explorer")

np.random.seed(int(seed))
walk = np.random.randn(int(steps)).cumsum()
df = pd.DataFrame({"value": walk})

c1.metric("Final value", f"{walk[-1]:.2f}")
c2.metric("Max", f"{walk.max():.2f}")
c3.metric("Min", f"{walk.min():.2f}")

st.line_chart(df)

with st.expander("See details"):
    st.write(f"Steps: {steps}, Seed: {seed}, Theme: {theme}")
    st.dataframe(df)

tab1, tab2 = st.tabs(["Chart", "Data"])
with tab1:
    st.line_chart(df)
with tab2:
    st.dataframe(df)

st.write(f"Button clicks: {st.session_state.count}")