from datetime import datetime, time

import streamlit as st

# Display app title and description.
st.title("Widget examples")
st.write("This app simply contains a couple of interactive widget examples.")

st.text_input("This is a one line text area.")
st.text_area("This is a text area spanning multiple lines.")
st.button("This is a clickable button.")
st.checkbox("This is a checkbox.")
st.radio(
    "This is a radio button with the second option preselected.",
    ["apple", "orange", "pear"],
    index=1,
)
st.selectbox(
    "This is a select box with the third option preselected.",
    ["apple", "orange", "pear"],
    index=2,
)
st.multiselect(
    "This multiselect allows you to select multiple options at once.",
    ["apple", "orange", "pear"],
)
st.slider(
    "A slider from 0-10 in steps of 2 with 4 as default",
    min_value=0,
    max_value=10,
    value=4,
    step=2,
)
st.number_input("This is a number input", min_value=0, max_value=100, value=50)

st.write("# Dealing with dates and time:")
st.date_input("Select a date with date input")
st.time_input("Select a time with time input")
st.slider("A date slider", value=datetime(2020, 1, 1, 9, 30), format="MM/DD/YY")
st.slider("A time slider", value=(time(10, 30), time(12, 30)))

st.write("# Upload a file")
st.file_uploader("Upload a file here (max. 200MB)")
