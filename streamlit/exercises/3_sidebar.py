import numpy as np

import streamlit as st

# Display app title and description.
st.title("Our First Streamlit App")
st.write("The description of our app, or some explanatory text.")

# Use st.sidebar.slider to create sliders in the side bar of  your app.
# YOUR CODE HERE START
# YOUR CODE HERE END

# Check whether period and amplitude variable exist
try:
    st.write(f"This is a sine with amplitude **{amplitude}** and period **{period}**.")
except NameError:
    st.error("You haven't created an amplitude/period variable", icon="🚨")

# Create a line chart with streamlit.
x = np.arange(0, 2 * np.pi, 0.01)
y = amplitude * np.sin(x * period)
st.line_chart(y)

# From the terminal run: streamlit run 3_sidebar.py
