import numpy as np

import streamlit as st

# Display title and description.
st.title("Our First Streamlit App")
st.write("The description of our app, or some explanatory text.")

# Create a slider forthe amplitude.
amplitude = st.slider("Amplitude", min_value=0, max_value=10, value=1)

# Add a slider for the period that ranges from 0 to 10.
# YOUR CODE HERE START
period = st.slider("Period", min_value=0, max_value=10, value=1)
# YOUR CODE HERE END

# Use st.write to display the information from the sliders.
# YOUR CODE HERE START
st.write(f"This is a sine with amplitude **{amplitude}** and period **{period}**.")
# YOUR CODE HERE END

# Create a range of values from 0 to 2*pi
x = np.arange(0, 2 * np.pi, 0.01)

# Multiply the variable x by the period
# YOUR CODE HERE START
x *= period
# YOUR CODE HERE END

# Create a line chart of a sine curve with controllable amplitude & period.
y = amplitude * np.sin(x)
st.line_chart(y)

# From the terminal run: streamlit run 2_line_chart_interaction.py
