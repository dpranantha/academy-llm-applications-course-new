import dotenv

import streamlit as st
from llm_in_production.llm import instantiate_langchain_model

dotenv.load_dotenv()


# Here we create the client.
# Make sure you select the LLM provider that corresponds to the one you are using in this course!
client = instantiate_langchain_model(
    llm_provider="azure",
    # llm_provider="gcp",
)

PAGE_TILE = "Custom LLM App"
st.set_page_config(page_title=PAGE_TILE, page_icon="📊")
st.title(PAGE_TILE)


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
