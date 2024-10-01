import numpy as np

import streamlit as st

# Display title and description.
st.title("Our First Streamlit App")
st.write("The description of our app, or some explanatory text.")

# Create a line chart of a sine curve with streamlit.
x = np.arange(0, 2 * np.pi, 0.01)
y = np.sin(x)
st.line_chart(y)

# From the terminal run: streamlit run 1_simple_line_chart.py
