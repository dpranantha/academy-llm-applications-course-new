import os

import pandas as pd

import streamlit as st

# Add a title
# YOUR CODE HERE START
# YOUR CODE HERE END


# Function to load the data.
def load_data():
    """Loads chickweight dataset."""
    return pd.read_csv(DATA_FILEPATH).rename(str.lower, axis="columns")


# Load the data, if possible.
DATA_FILEPATH = "data/chickweight.csv"
try:
    chickweight = load_data()
except FileNotFoundError:
    st.error(
        f"Can't find the dataset, current working directory is: {os.getcwd()}", icon="🚨"
    )

# Set the min/max time.
# YOUR CODE HERE START
# YOUR CODE HERE END

# Add a slider to the sidebar to select the times to filer on.
# YOUR CODE HERE START
# YOUR CODE HERE END

# Add a checkbox to the sidebar to select the diets to show.
# YOUR CODE HERE START
# YOUR CODE HERE END

# filter the data according to the time range and selected diets.
filtered_data = (
    chickweight
    # YOUR CODE HERE START
    # YOUR CODE HERE END
)

# plot the filtered data
st.line_chart(
    filtered_data.groupby(["time", "diet"])["weight"].mean().unstack(),
)

# From the terminal run: streamlit run 5_pandas_assignment.py
