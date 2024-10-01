from pathlib import Path

import streamlit as st

title = "Streamlit Exercise"
st.set_page_config(
    page_title=title,
    page_icon="👋",
)
st.title(title)

with open(Path(__file__).parent / "readme.md") as f:
    st.markdown(f.read())
