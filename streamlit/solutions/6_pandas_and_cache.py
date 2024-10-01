# From the terminal run: streamlit run 6_pandas_and_cache.py
import os
from datetime import time

import pandas as pd

import streamlit as st

# Write title in main view.
st.title("NYC Uber Pick-ups Demo")
st.write(
    "Simple demo to illustrate the usefulness of `st.cache.` and the use of `st.map`."
)


# Use the st.cache_data decorator to prevent re-loading the data.
@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_FILEPATH, nrows=nrows).rename(str.lower, axis="columns")
    data["datetime"] = pd.to_datetime(data["date/time"])
    return data


# Load the data, if possible.
DATA_FILEPATH = "data/uber-raw-data-sep14.csv.gz"
try:
    data = load_data(100000)
except FileNotFoundError:
    st.error(
        f"Can't find the dataset, current working directory is: {os.getcwd()}", icon="🚨"
    )

# Controls.
st.sidebar.markdown("# Controls")

# Add a `date_input` to the sidebar to select the date range to show.
# YOUR CODE HERE START
first_date = data["datetime"].min()
last_date = data["datetime"].max()
date = st.sidebar.date_input(
    "Date", min_value=first_date, max_value=last_date, value=first_date
)
# YOUR CODE HERE END

# A slider to the range of times to show.
time_start, time_end = st.sidebar.slider("Time", value=(time(9, 00), time(12, 30)))

# Filter the data on the selected dates and time.
filtered_data = (
    data
    # YOUR CODE HERE START
    .loc[lambda d: d["datetime"].dt.date == date]
    # YOUR CODE HERE END
    .loc[lambda d: d["datetime"].dt.time >= time_start].loc[
        lambda d: d["datetime"].dt.time <= time_end
    ]
)

# Create a map. The Pandas dataframe must contain a lat and lon column.
st.map(filtered_data)

# Add a checkbox to show the raw data.
# YOUR CODE HERE START
if st.sidebar.checkbox("Show raw data"):
    st.write(filtered_data)
# YOUR CODE HERE END
