import os

import pandas as pd

import streamlit as st

# Write the title in main view.
st.write("# Chickweight dataset")


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

# Select diet in the sidebar: one option to select.
diet = st.sidebar.selectbox("Select diet", chickweight["diet"].unique())

# Use st.multiselect to select the (multiple) columns to filer on.
# YOUR CODE HERE START
# YOUR CODE HERE END

# Filter the chickweight based on the selection of diet and columns.
filtered_chickweight = (
    chickweight.loc[lambda d: d["diet"] == diet]
    # YOUR CODE HERE START
    # YOUR CODE HERE END
)
# Display filtered chickweight in main view.
st.write(filtered_chickweight)

# From the terminal run: streamlit run 4_pandas.py
