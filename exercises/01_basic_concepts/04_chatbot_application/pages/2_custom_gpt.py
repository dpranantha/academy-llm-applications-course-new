import dotenv

import streamlit as st
from llm_in_production.openai_utils import get_openai_client

PAGE_TILE = "Custom LLM App"
st.set_page_config(page_title=PAGE_TILE, page_icon="📊")
st.title(PAGE_TILE)


dotenv.load_dotenv()
client = get_openai_client()

with st.sidebar:
    st.header("Settings")
    st.write("TODO...")


# Accept user input
prompt = st.chat_input("Add your text here")

if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.write("TODO...")